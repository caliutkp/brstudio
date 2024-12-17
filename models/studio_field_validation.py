from odoo import models, api
from odoo.exceptions import ValidationError
import re

class StudioFieldValidation(models.AbstractModel):
    _name = 'studio.field.validation'
    _description = 'Studio Field Validation Logic'

    @api.model
    def validate_field_name(self, name):
        """Validate field name format"""
        if not name:
            raise ValidationError('Field name cannot be empty')
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
            raise ValidationError('Invalid field name format')
        return True

    @api.model
    def validate_field_type(self, field_type, relation=None):
        """Validate field type and its requirements"""
        if field_type in ['many2one', 'one2many', 'many2many'] and not relation:
            raise ValidationError(f'{field_type} requires a relation model')
        return True