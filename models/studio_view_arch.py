from odoo import models, api
from lxml import etree

class StudioViewArch(models.AbstractModel):
    _name = 'studio.view.arch'
    _description = 'View Architecture Builder'

    @api.model
    def build_arch(self, view_type, components, options=None):
        """Build view architecture from components"""
        root = self._create_root_element(view_type)
        self._add_components(root, components, options)
        return etree.tostring(root, pretty_print=True, encoding='unicode')
    
    def _create_root_element(self, view_type):
        """Create root element based on view type"""
        root = etree.Element(view_type)
        if view_type == 'form':
            sheet = etree.SubElement(root, 'sheet')
            return sheet
        return root
    
    def _add_components(self, parent, components, options):
        """Add components to parent element"""
        for component in sorted(components, key=lambda c: c.get('sequence', 0)):
            element = self._create_component_element(parent, component)
            if component.get('components'):
                self._add_components(element, component['components'], options)