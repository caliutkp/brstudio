from odoo import models, api
from odoo.exceptions import ValidationError

class StudioAPIAuth(models.AbstractModel):
    _name = 'studio.api.auth'
    _description = 'API Authentication Handler'

    @api.model
    def prepare_auth_headers(self, auth_type, api_key):
        """Prepare authentication headers based on type"""
        headers = {'Content-Type': 'application/json'}
        
        if auth_type == 'bearer':
            headers['Authorization'] = f'Bearer {api_key}'
        elif auth_type == 'basic':
            headers['Authorization'] = f'Basic {api_key}'
        elif auth_type == 'api_key':
            headers['X-API-Key'] = api_key
        else:
            raise ValidationError(f'Unsupported authentication type: {auth_type}')
            
        return headers
    
    @api.model
    def validate_auth_config(self, auth_type, api_key):
        """Validate authentication configuration"""
        if not api_key:
            raise ValidationError('API key is required')
            
        if auth_type not in ['bearer', 'basic', 'api_key']:
            raise ValidationError(f'Invalid authentication type: {auth_type}')