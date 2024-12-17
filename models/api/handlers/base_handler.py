from odoo import models, api
import requests
from odoo.exceptions import ValidationError

class BaseHandler(models.AbstractModel):
    _name = 'studio.api.handler.base'
    _description = 'Base API Handler'

    def _make_request(self, method, url, headers, data=None, timeout=30):
        """Make HTTP request with error handling"""
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValidationError(f'API Request failed: {str(e)}')