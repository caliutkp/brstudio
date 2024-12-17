from odoo import models, api
from odoo.exceptions import ValidationError
from lxml import etree

class StudioViewValidator(models.AbstractModel):
    _name = 'studio.view.validator'
    _description = 'View Validation Logic'

    @api.model
    def validate_view(self, view_data):
        """Validate complete view configuration"""
        self._validate_basic_data(view_data)
        self._validate_components(view_data.get('components', []))
        if view_data.get('arch'):
            self._validate_arch(view_data['arch'])
        return True
    
    def _validate_basic_data(self, view_data):
        """Validate basic view data"""
        if not view_data.get('name'):
            raise ValidationError('View name is required')
        if not view_data.get('model_id'):
            raise ValidationError('Model is required')
        if not view_data.get('view_type'):
            raise ValidationError('View type is required')
    
    def _validate_components(self, components):
        """Validate view components"""
        for component in components:
            if not component.get('type'):
                raise ValidationError('Component type is required')
            self._validate_component_attributes(component)
            if component.get('components'):
                self._validate_components(component['components'])
    
    def _validate_arch(self, arch):
        """Validate XML architecture"""
        try:
            etree.fromstring(arch)
        except etree.XMLSyntaxError as e:
            raise ValidationError(f'Invalid view architecture: {str(e)}')