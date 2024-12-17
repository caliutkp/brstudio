from odoo import models, api
from odoo.exceptions import UserError
from typing import Dict, Any

class APIErrorHandler(models.AbstractModel):
    _name = 'studio.api.error.handler'
    _description = 'API Error Handler'

    @api.model
    def handle_error(self, error: Exception, context: Dict[str, Any] = None) -> None:
        """Handle API errors"""
        error_message = str(error)
        
        if context and context.get('connection'):
            connection = context['connection']
            connection.write({
                'state': 'failed',
                'last_status': error_message
            })
            
        if isinstance(error, UserError):
            raise error
            
        raise UserError(f'API Error: {error_message}')