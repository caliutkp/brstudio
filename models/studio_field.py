from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudioField(models.Model):
    _name = 'studio.field'
    _description = 'Studio Field Configuration'
    _inherit = ['studio.mixin']

    name = fields.Char(string='Field Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    field_type = fields.Selection([
        ('char', 'Text'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('date', 'Date'),
        ('datetime', 'Date & Time'),
        ('boolean', 'Boolean'),
        ('many2one', 'Many2One'),
        ('one2many', 'One2Many'),
        ('many2many', 'Many2Many'),
    ], string='Field Type', required=True)
    
    @api.model
    def create_field(self, vals):
        """Create a new field in the specified model"""
        self._validate_field_values(vals)
        return self._create_field_in_model(vals)
    
    def _validate_field_values(self, vals):
        """Validate field values before creation"""
        if not self._is_valid_field_name(vals.get('name')):
            raise ValidationError('Invalid field name')