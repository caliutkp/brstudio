from odoo import http
from odoo.http import request

class StudioFieldController(http.Controller):
    @http.route('/studio/field/create', type='json', auth='user')
    def create_field(self, **kwargs):
        """Handle field creation requests"""
        return request.env['studio.field'].create_field(kwargs)
    
    @http.route('/studio/field/preview', type='json', auth='user')
    def preview_field(self, field_data):
        """Preview field before creation"""
        return self._generate_field_preview(field_data)