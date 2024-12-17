from odoo import models, fields

class StudioFieldType(models.Model):
    _name = 'studio.field.type'
    _description = 'Field Type Configuration'
    
    name = fields.Char(string='Type Name', required=True)
    technical_name = fields.Char(string='Technical Name', required=True)
    has_size = fields.Boolean(string='Has Size Parameter')
    has_digits = fields.Boolean(string='Has Digits Parameter')
    category = fields.Selection([
        ('basic', 'Basic'),
        ('numeric', 'Numeric'),
        ('relational', 'Relational'),
        ('special', 'Special')
    ], string='Category', required=True)
    default_values = fields.Text(string='Default Values Config')