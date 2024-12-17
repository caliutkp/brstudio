from odoo import models, fields, api

class StudioView(models.Model):
    _name = 'studio.view'
    _description = 'Studio View Configuration'

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
    
    def generate_view_xml(self):
        """Generate XML architecture for the view"""
        return self._build_view_xml()