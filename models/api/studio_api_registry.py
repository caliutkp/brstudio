from odoo import models, fields, api

class StudioAPIRegistry(models.Model):
    _name = 'studio.api.registry'
    _description = 'API Registry'
    
    name = fields.Char(string='Name', required=True)
    provider_id = fields.Many2one('studio.api.provider', required=True)
    endpoint_ids = fields.One2many('studio.api.endpoint', 'registry_id')
    documentation_url = fields.Char(string='Documentation URL')
    description = fields.Text()
    
    _sql_constraints = [
        ('name_provider_uniq', 'unique(name, provider_id)', 
         'API name must be unique per provider!')
    ]