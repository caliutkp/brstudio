from odoo import models, api
from typing import Dict, Any

class APIResponseHandler(models.AbstractModel):
    _name = 'studio.api.response.handler'
    _description = 'API Response Handler'

    @api.model
    def process_response(self, response) -> Dict[str, Any]:
        """Process API response"""
        try:
            return {
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'data': response.json() if response.text else {},
                'raw': response.text,
            }
        except ValueError:
            return {
                'status_code': response.status_code,
                'headers': dict(response.headers),
                'data': {},
                'raw': response.text,
            }