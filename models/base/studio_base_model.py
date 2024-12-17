from odoo import models, fields, api

class StudioBaseModel(models.AbstractModel):
    _name = 'studio.base'
    _description = 'Studio Base Model'
    _inherit = ['studio.mixin']

    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    create_date = fields.Datetime(readonly=True)
    write_date = fields.Datetime(readonly=True)
    
    def _get_studio_context(self):
        """Get common studio context"""
        return {
            'studio_version': self.env['ir.config_parameter'].get_param('studio.version'),
            'user_has_group_studio': self.env.user.has_group('studio.group_studio_user'),
        }