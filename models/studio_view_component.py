from odoo import models, fields

class StudioViewComponent(models.Model):
    _name = 'studio.view.component'
    _description = 'View Component Configuration'
    
    name = fields.Char(string='Component Name', required=True)
    view_id = fields.Many2one('studio.view', string='View', required=True)
    component_type = fields.Selection([
        ('field', 'Field'),
        ('button', 'Button'),
        ('group', 'Group'),
        ('notebook', 'Notebook')
    ], string='Component Type', required=True)
    sequence = fields.Integer(string='Sequence')
    parent_id = fields.Many2one('studio.view.component', string='Parent Component')
    child_ids = fields.One2many('studio.view.component', 'parent_id', string='Child Components')
    attrs = fields.Text(string='Attributes')