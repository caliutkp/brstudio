from odoo import models, api
from odoo.exceptions import ValidationError

class StudioValidator(models.AbstractModel):
    _name = 'studio.validator'
    _description = 'Base Validation Logic'

    @api.model
    def validate_name(self, name, pattern=None):
        """Validate name format"""
        if not name:
            raise ValidationError('Name cannot be empty')
            
        if pattern and not pattern.match(name):
            raise ValidationError('Invalid name format')
        
        return True
    
    @api.model
    def validate_required_fields(self, values, required_fields):
        """Validate required fields"""
        missing_fields = [field for field in required_fields if not values.get(field)]
        if missing_fields:
            raise ValidationError(f'Missing required fields: {", ".join(missing_fields)}')