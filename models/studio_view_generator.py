from odoo import models, api
from ..utils import xml_utils

class StudioViewGenerator(models.AbstractModel):
    _name = 'studio.view.generator'
    _description = 'Studio View Generation Logic'

    @api.model
    def generate_view_xml(self, view_type, components, options=None):
        """Generate view XML from components"""
        return xml_utils.create_view_xml(
            view_type=view_type,
            fields=components,
            options=options
        )
    
    @api.model
    def generate_view_preview(self, view_data):
        """Generate preview of view changes"""
        components = self.env['studio.view.component'].search([
            ('view_id', '=', view_data['view_id'])
        ])
        return self.generate_view_xml(
            view_data['view_type'],
            components,
            view_data.get('options')
        )