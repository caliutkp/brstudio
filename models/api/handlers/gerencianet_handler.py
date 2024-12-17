from odoo import models, api
from odoo.exceptions import ValidationError
import requests

class GerenciaNetHandler(models.AbstractModel):
    _name = 'studio.api.handler.gerencianet'
    _description = 'GerenciaNet API Handler'

    @api.model
    def create_charge(self, provider_id, items):
        """Create a new charge"""
        provider = self.env['studio.api.provider.gerencianet'].browse(provider_id)
        
        endpoint = f"{provider._get_api_endpoint()}/v1/charge"
        headers = provider._prepare_auth_headers()
        
        try:
            response = requests.post(
                endpoint,
                json={'items': items},
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise ValidationError(f'GerenciaNet API Request failed: {str(e)}')