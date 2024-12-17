from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StudioFieldBase(models.Model):
    _name = 'studio.field'
    _description = 'Studio Field Base Configuration'
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
    
    _sql_constraints = [
        ('name_model_uniq', 'unique(name, model_id)', 
         'Field name must be unique per model!')
    ]