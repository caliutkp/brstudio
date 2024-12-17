from odoo import models, api
from odoo.exceptions import ValidationError

class StudioViewManager(models.Model):
    _name = 'studio.view'
    _inherit = ['studio.view.base']
    _description = 'Studio View Manager'

    @api.model
    def create_view(self, vals):
        """Main entry point for view creation"""
        # Generate view architecture
        generator = self.env['studio.view.generator']
        components = vals.get('components', [])
        arch = generator.generate_view_xml(
            vals['view_type'],
            components,
            vals.get('options')
        )
        
        # Validate view
        validator = self.env['studio.view.validator']
        validator.validate_view_arch(arch)
        validator.validate_view_fields(vals['model_id'], 
            [c['name'] for c in components if 'name' in c])
        
        # Create view record
        vals['arch'] = arch
        view = self.create(vals)
        
        # Create actual view in ir.ui.view
        ir_view = self._create_ir_view(view)
        
        return {
            'view_id': view.id,
            'ir_view_id': ir_view.id,
        }
    
    def _create_ir_view(self, studio_view):
        """Create view in ir.ui.view"""
        return self.env['ir.ui.view'].create({
            'name': studio_view.name,
            'model': studio_view.model_id.model,
            'type': studio_view.view_type,
            'arch_base': studio_view.arch,
            'inherit_id': False,
            'mode': 'extension',
        })