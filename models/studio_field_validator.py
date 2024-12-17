from odoo import models, api
from odoo.exceptions import ValidationError
import re

class StudioFieldValidator(models.AbstractModel):
    _name = 'studio.field.validator'
    _description = 'Field Validation Logic'

    @api.model
    def validate_field_config(self, vals):
        """Validate complete field configuration"""
        errors = []
        
        # Validate field name
        if not self._is_valid_name(vals.get('name', '')):
            errors.append('Invalid field name format')
            
        # Validate field type
        if not self._is_valid_type(vals.get('field_type')):
            errors.append('Invalid field type')
            
        # Validate relational fields
        if self._is_relational_type(vals.get('field_type')) and not vals.get('relation'):
            errors.append('Relation model required for relational fields')
            
        if errors:
            raise ValidationError('\n'.join(errors))
        
        return True
    
    def _is_valid_name(self, name):
        """Check if field name follows Python identifier rules"""
        if not name:
            return False
        return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))
    
    def _is_valid_type(self, field_type):
        """Check if field type is supported"""
        valid_types = self.env['studio.field.type'].search([]).mapped('technical_name')
        return field_type in valid_types
    
    def _is_relational_type(self, field_type):
        """Check if field type is relational"""
        return field_type in ['many2one', 'one2many', 'many2many']