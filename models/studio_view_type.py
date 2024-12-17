from odoo import models, fields

class StudioViewType(models.Model):
    _name = 'studio.view.type'
    _description = 'View Type Configuration'
    
    name = fields.Char(string='Display Name', required=True)
    technical_name = fields.Selection([
        ('form', 'Form'),
        ('tree', 'List'),
        ('kanban', 'Kanban'),
        ('calendar', 'Calendar'),
        ('pivot', 'Pivot'),
    ], string='Technical Name', required=True)
    
    allowed_components = fields.Many2many('studio.component.type', string='Allowed Components')
    default_options = fields.Text(string='Default Configuration')
    
    _sql_constraints = [
        ('technical_name_uniq', 'unique(technical_name)', 
         'Technical name must be unique!')
    ]