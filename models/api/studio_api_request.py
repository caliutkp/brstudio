from odoo import models, fields, api
import requests
import time
from odoo.exceptions import UserError

class StudioAPIRequest(models.AbstractModel):
    _name = 'studio.api.request'
    _description = 'API Request Handler'

    def execute_request(self, connection, method, endpoint, data=None):
        """Execute API request with logging"""
        start_time = time.time()
        request_data = {
            'url': endpoint,
            'method': method,
            'headers': connection._prepare_headers(),
            'body': data
        }
        
        try:
            response = self._make_request(request_data)
            duration = time.time() - start_time
            
            # Log the request
            self.env['studio.api.response']._log_request(
                connection, request_data, response, duration)
            
            return response
            
        except Exception as e:
            self._handle_request_error(e, connection)
    
    def _make_request(self, request_data):
        """Make the actual HTTP request"""
        try:
            response = requests.request(
                method=request_data['method'],
                url=request_data['url'],
                headers=request_data['headers'],
                json=request_data.get('body'),
                timeout=30
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise UserError(f'API Request failed: {str(e)}')
    
    def _handle_request_error(self, error, connection):
        """Handle request errors"""
        error_message = str(error)
        connection.write({
            'state': 'failed',
            'last_status': error_message
        })
        raise UserError(f'API Request failed: {error_message}')