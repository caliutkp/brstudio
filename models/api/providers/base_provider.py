from odoo import models, fields

class BaseProvider(models.AbstractModel):
    _name = 'studio.api.provider.base'
    _description = 'Base API Provider'
    _inherit = ['studio.api.base', 'studio.api.mixin']

    provider_type = fields.Selection([
        ('openai', 'OpenAI'),
        ('gerencianet', 'GerenciaNet')
    ], string='Provider Type', required=True)
    
    timeout = fields.Integer(string='Timeout (seconds)', default=30)
    retry_count = fields.Integer(string='Retry Count', default=3)