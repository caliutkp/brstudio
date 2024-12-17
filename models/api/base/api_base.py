from odoo import models, fields, api
from odoo.exceptions import ValidationError

class APIBase(models.AbstractModel):
    _name = 'studio.api.base'
    _description = 'Base API Model'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    api_key = fields.Char(string='API Key', required=True)
    endpoint = fields.Char(string='Endpoint', required=True)
    
    def _validate_connection(self):
        """Validate API connection"""
        self.ensure_one()
        if not self.api_key or not self.endpoint:
            raise ValidationError('API key and endpoint are required')