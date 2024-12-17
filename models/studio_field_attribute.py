from odoo import models, fields

class StudioFieldAttribute(models.Model):
    _name = 'studio.field.attribute'
    _description = 'Field Attribute Configuration'
    
    name = fields.Char(string='Attribute Name', required=True)
    field_id = fields.Many2one('studio.field', string='Field', required=True)
    attr_type = fields.Selection([
        ('size', 'Size'),
        ('digits', 'Digits'),
        ('domain', 'Domain'),
        ('selection', 'Selection Values')
    ], string='Attribute Type')
    value = fields.Text(string='Value')