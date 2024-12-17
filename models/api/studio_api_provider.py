from odoo import models, fields

class StudioAPIProvider(models.Model):
    _name = 'studio.api.provider'
    _description = 'API Provider Configuration'

    name = fields.Char(string='Provider Name', required=True)
    code = fields.Char(string='Provider Code', required=True)
    base_url = fields.Char(string='Base URL')
    auth_type = fields.Selection([
        ('bearer', 'Bearer Token'),
        ('basic', 'Basic Auth'),
        ('api_key', 'API Key'),
    ], string='Authentication Type', required=True)
    headers_template = fields.Text(string='Headers Template')
    
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Provider code must be unique!')
    ]