from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GerenciaNetProvider(models.Model):
    _name = 'studio.api.provider.gerencianet'
    _inherit = ['studio.api.provider']
    _description = 'GerenciaNet API Provider'

    sandbox_mode = fields.Boolean(string='Sandbox Mode', default=True)
    client_id = fields.Char(string='Client ID', required=True)
    client_secret = fields.Char(string='Client Secret', required=True)
    
    def _get_api_endpoint(self):
        """Get appropriate API endpoint based on mode"""
        return 'https://api-pix-h.gerencianet.com.br' if self.sandbox_mode else 'https://api-pix.gerencianet.com.br'
    
    def _prepare_auth_headers(self):
        """Prepare GerenciaNet authentication headers"""
        credentials = f"{self.client_id}:{self.client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/json'
        }