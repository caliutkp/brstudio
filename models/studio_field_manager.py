from odoo import models, api
from odoo.exceptions import ValidationError

class StudioFieldManager(models.Model):
    _name = 'studio.field'
    _inherit = ['studio.mixin']
    _description = 'Field Management'

    @api.model
    def create_field(self, vals):
        """Main entry point for field creation"""
        # Validate field configuration
        validator = self.env['studio.field.validator']
        validator.validate_field_config(vals)
        
        # Generate field definition
        generator = self.env['studio.field.generator']
        field_def = generator.generate_field_definition(vals)
        
        # Create field in ir.model.fields
        model_field = self.env['ir.model.fields'].create(field_def)
        
        # Create studio field record
        studio_field = self.create({
            'name': vals['name'],
            'model_id': vals['model_id'],
            'field_type': vals['field_type'],
        })
        
        # Create field properties
        self._create_field_properties(studio_field, vals)
        
        return {
            'studio_field_id': studio_field.id,
            'model_field_id': model_field.id,
        }
        
    def _create_field_properties(self, field, vals):
        """Create field properties"""
        property_obj = self.env['studio.field.property']
        
        # Map values to properties
        properties = []
        if vals.get('size'):
            properties.append(('size', str(vals['size'])))
        if vals.get('digits'):
            properties.append(('digits', str(vals['digits'])))
        if vals.get('relation'):
            properties.append(('relation', vals['relation']))
        
        # Create property records
        for prop_type, value in properties:
            property_obj.create({
                'field_id': field.id,
                'property_type': prop_type,
                'value': value,
            })