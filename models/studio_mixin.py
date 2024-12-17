from odoo import models, api

class StudioMixin(models.AbstractModel):
    _name = 'studio.mixin'
    _description = 'Studio Mixin for Common Functionality'

    @api.model
    def _get_studio_properties(self):
        """Get common studio properties"""
        return {
            'is_studio_enabled': True,
            'studio_version': self.env['ir.config_parameter'].get_param('studio.version', '1.0'),
        }

    def _validate_studio_operation(self, operation):
        """Validate studio operations"""
        return True  # Implement validation logic