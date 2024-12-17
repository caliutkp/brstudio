from odoo import models, api

class StudioFieldGenerator(models.AbstractModel):
    _name = 'studio.field.generator'
    _description = 'Field Generation Logic'

    @api.model
    def generate_field_definition(self, field_config):
        """Generate field definition for model"""
        field_def = {
            'name': f"x_{field_config['name']}",
            'field_description': field_config['name'],
            'ttype': field_config['field_type'],
            'model_id': field_config['model_id'],
        }
        
        # Add properties based on field type
        type_config = self.env['studio.field.type'].get_type_config(field_config['field_type'])
        
        if type_config.get('has_relation') and field_config.get('relation'):
            field_def['relation'] = field_config['relation']
            
        if type_config.get('has_size') and field_config.get('size'):
            field_def['size'] = field_config['size']
            
        if type_config.get('has_digits') and field_config.get('digits'):
            field_def['digits'] = field_config['digits']
            
        return field_def