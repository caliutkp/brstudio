from odoo import models, api
from odoo.exceptions import ValidationError

class StudioFieldCreator(models.AbstractModel):
    _name = 'studio.field.creator'
    _description = 'Studio Field Creation Logic'

    @api.model
    def create_field_in_model(self, vals):
        """Create field in the target model"""
        model = self.env['ir.model'].browse(vals['model_id'])
        
        field_data = {
            'model_id': model.id,
            'name': f"x_{vals['name']}",
            'field_description': vals['name'],
            'ttype': vals['field_type'],
        }
        
        if vals.get('relation_model'):
            field_data['relation'] = vals['relation_model']
            
        return self.env['ir.model.fields'].create(field_data)