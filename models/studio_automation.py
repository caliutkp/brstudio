from odoo import models, fields, api

class StudioAutomation(models.Model):
    _name = 'studio.automation'
    _description = 'Studio Automation Rules'

    name = fields.Char(string='Rule Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    trigger = fields.Selection([
        ('on_create', 'On Creation'),
        ('on_write', 'On Update'),
        ('on_unlink', 'On Deletion'),
    ], string='Trigger', required=True)
    condition = fields.Text(string='Condition', help='Python expression for condition')
    action = fields.Text(string='Action', help='Python code to execute')
    
    def execute_automation(self, record):
        """Execute the automation rule"""
        if self._evaluate_condition(record):
            return self._execute_action(record)