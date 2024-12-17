from odoo import models, fields

class StudioAPIEndpoint(models.Model):
    _name = 'studio.api.endpoint'
    _description = 'API Endpoint Configuration'
    
    name = fields.Char(string='Name', required=True)
    registry_id = fields.Many2one('studio.api.registry', required=True)
    path = fields.Char(string='Endpoint Path', required=True)
    method = fields.Selection([
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    ], string='HTTP Method', required=True)
    requires_auth = fields.Boolean(string='Requires Authentication', default=True)
    request_schema = fields.Text(string='Request Schema')
    response_schema = fields.Text(string='Response Schema')