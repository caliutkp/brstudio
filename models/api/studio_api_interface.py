from odoo import models, api
from typing import Dict, Any, Optional

class StudioAPIInterface(models.AbstractModel):
    _name = 'studio.api.interface'
    _description = 'API Interface Definition'

    @api.model
    def execute_request(self, 
                       connection_id: int, 
                       method: str, 
                       endpoint: str, 
                       data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute API request through connection"""
        connection = self.env['studio.api.connection'].browse(connection_id)
        request_handler = self.env['studio.api.request']
        return request_handler.execute_request(connection, method, endpoint, data)