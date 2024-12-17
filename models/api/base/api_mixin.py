from odoo import models, api
from odoo.exceptions import ValidationError

class APIMixin(models.AbstractModel):
    _name = 'studio.api.mixin'
    _description = 'API Mixin'

    def _prepare_headers(self):
        """Prepare request headers"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
    
    def _validate_response(self, response):
        """Validate API response"""
        if response.get('error'):
            raise ValidationError(f"API Error: {response['error']}")