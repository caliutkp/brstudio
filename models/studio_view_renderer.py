from odoo import models, api

class StudioViewRenderer(models.AbstractModel):
    _name = 'studio.view.renderer'
    _description = 'View Rendering Logic'

    @api.model
    def render_preview(self, view_data):
        """Render view preview"""
        arch_builder = self.env['studio.view.arch']
        arch = arch_builder.build_arch(
            view_data['view_type'],
            view_data.get('components', []),
            view_data.get('options')
        )
        
        return {
            'arch': arch,
            'model': self.env['ir.model'].browse(view_data['model_id']).model,
            'type': view_data['view_type'],
        }
    
    @api.model
    def render_editor(self, view_id):
        """Render view editor"""
        view = self.env['studio.view'].browse(view_id)
        return {
            'view_data': view.read()[0],
            'components': self._get_available_components(view.view_type),
            'model_fields': self._get_model_fields(view.model_id),
        }
    
    def _get_available_components(self, view_type):
        """Get available components for view type"""
        view_type_record = self.env['studio.view.type'].search(
            [('technical_name', '=', view_type)], limit=1)
        return view_type_record.allowed_components.read(['name', 'technical_name', 'category'])
    
    def _get_model_fields(self, model_id):
        """Get available fields for model"""
        return self.env['ir.model.fields'].search_read(
            [('model_id', '=', model_id)],
            ['name', 'field_description', 'ttype']
        )