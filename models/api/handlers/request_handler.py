from odoo import models, api
from odoo.exceptions import UserError
import requests
import time
from typing import Dict, Any, Optional

class APIRequestHandler(models.AbstractModel):
    _name = 'studio.api.request.handler'
    _description = 'API Request Handler'

    def execute_request(self, connection, method: str, endpoint: str, 
                       data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute and log API request"""
        start_time = time.time()
        
        try:
            response = self._make_request(connection, method, endpoint, data)
            duration = time.time() - start_time
            
            self._log_response(connection, method, endpoint, data, response, duration)
            return self._process_response(response)
            
        except Exception as e:
            self._handle_error(connection, e)
    
    def _make_request(self, connection, method: str, endpoint: str, 
                     data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Make HTTP request"""
        try:
            return requests.request(
                method=method,
                url=endpoint,
                headers=connection._prepare_headers(),
                json=data,
                timeout=connection.timeout
            )
        except requests.exceptions.RequestException as e:
            raise UserError(f'Request failed: {str(e)}')