from odoo import models, fields, api

class StudioViewBase(models.Model):
    _name = 'studio.view'
    _description = 'Studio View Base Configuration'
    _inherit = ['studio.mixin']

    name = fields.Char(string='View Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    view_type = fields.Selection([
        ('form', 'Form'),
        ('tree', 'List'),
        ('kanban', 'Kanban'),
        ('calendar', 'Calendar'),
        ('pivot', 'Pivot'),
    ], string='View Type', required=True)
    arch = fields.Text(string='View Architecture')
    is_custom = fields.Boolean(string='Is Custom View', default=True)
    sequence = fields.Integer(string='Sequence', default=10)
    
    _sql_constraints = [
        ('name_model_type_uniq', 'unique(name, model_id, view_type)', 
         'View name must be unique per model and type!')
    ]