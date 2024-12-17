from odoo import models, fields

class StudioComponentType(models.Model):
    _name = 'studio.component.type'
    _description = 'View Component Type'
    
    name = fields.Char(string='Display Name', required=True)
    technical_name = fields.Selection([
        ('field', 'Field'),
        ('button', 'Button'),
        ('group', 'Group'),
        ('notebook', 'Notebook'),
        ('page', 'Notebook Page'),
        ('separator', 'Separator'),
    ], string='Technical Name', required=True)
    
    category = fields.Selection([
        ('basic', 'Basic'),
        ('container', 'Container'),
        ('action', 'Action'),
    ], string='Category', required=True)
    
    allowed_attributes = fields.Text(string='Allowed Attributes')
    template = fields.Text(string='Component Template')