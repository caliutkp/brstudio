from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudioAPIBase(models.AbstractModel):
    _name = 'studio.api.base'
    _description = 'Base API Model'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    provider_id = fields.Many2one('studio.api.provider', string='API Provider', required=True)
    api_key = fields.Char(string='API Key', required=True)
    endpoint = fields.Char(string='Endpoint', required=True)
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'API connection name must be unique!')
    ]

    def _validate_connection(self):
        """Validate API connection"""
        self.ensure_one()
        if not self.api_key or not self.endpoint:
            raise ValidationError('API key and endpoint are required')