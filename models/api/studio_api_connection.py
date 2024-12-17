from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudioAPIConnection(models.Model):
    _name = 'studio.api.connection'
    _inherit = ['studio.api.base']
    _description = 'API Connection Manager'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('failed', 'Failed')
    ], default='draft', string='Status')
    last_status = fields.Text(string='Last Status', readonly=True)
    retry_count = fields.Integer(string='Retry Count', default=3)
    timeout = fields.Integer(string='Timeout (seconds)', default=30)
    
    def action_test_connection(self):
        """Test API connection"""
        self.ensure_one()
        try:
            self._validate_connection()
            request_handler = self.env['studio.api.request']
            response = request_handler.execute_request(
                self, 'GET', self.endpoint)
            
            self.write({
                'state': 'validated',
                'last_status': response.text if response else 'Success'
            })
        except Exception as e:
            self.write({
                'state': 'failed',
                'last_status': str(e)
            })
    
    def _prepare_headers(self):
        """Prepare request headers with authentication"""
        auth_handler = self.env['studio.api.auth']
        return auth_handler.prepare_auth_headers(
            self.provider_id.auth_type, 
            self.api_key
        )