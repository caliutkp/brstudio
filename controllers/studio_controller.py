from odoo import http
from odoo.http import request

class StudioController(http.Controller):
    @http.route('/studio/info', type='json', auth='user')
    def get_studio_info(self):
        """Get general studio information"""
        return {
            'version': request.env['ir.config_parameter'].get_param('studio.version', '1.0'),
            'available_models': self._get_available_models(),
        }
    
    def _get_available_models(self):
        """Get list of models available for customization"""
        return request.env['ir.model'].search_read([], ['name', 'model'])