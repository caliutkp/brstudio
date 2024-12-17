from odoo import models, fields, api

class StudioFieldProperty(models.Model):
    _name = 'studio.field.property'
    _description = 'Field Property Configuration'
    
    field_id = fields.Many2one('studio.field', string='Field', required=True)
    property_type = fields.Selection([
        ('size', 'Size'),
        ('digits', 'Digits'),
        ('domain', 'Domain'),
        ('selection', 'Selection Values'),
        ('relation', 'Related Model'),
        ('required', 'Required'),
        ('readonly', 'Read Only'),
        ('store', 'Stored'),
        ('index', 'Indexed'),
        ('copy', 'Copied'),
        ('translate', 'Translatable'),
    ], string='Property Type', required=True)
    value = fields.Text(string='Property Value')
    
    _sql_constraints = [
        ('field_property_uniq', 'unique(field_id, property_type)', 
         'Property type must be unique per field!')
    ]