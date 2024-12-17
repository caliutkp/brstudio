from odoo import models, fields
import json

class StudioAPIResponse(models.Model):
    _name = 'studio.api.response'
    _description = 'API Response Log'
    _order = 'create_date desc'

    connection_id = fields.Many2one('studio.api.connection', string='API Connection')
    request_url = fields.Char(string='Request URL')
    request_method = fields.Char(string='HTTP Method')
    request_headers = fields.Text(string='Request Headers')
    request_body = fields.Text(string='Request Body')
    response_code = fields.Integer(string='Response Code')
    response_headers = fields.Text(string='Response Headers')
    response_body = fields.Text(string='Response Body')
    duration = fields.Float(string='Duration (s)', digits=(16, 4))
    
    def _log_request(self, connection, request, response, duration):
        """Log API request and response"""
        return self.create({
            'connection_id': connection.id,
            'request_url': request.get('url'),
            'request_method': request.get('method'),
            'request_headers': json.dumps(request.get('headers')),
            'request_body': json.dumps(request.get('body')),
            'response_code': response.status_code if response else 0,
            'response_headers': json.dumps(dict(response.headers)) if response else '',
            'response_body': response.text if response else '',
            'duration': duration,
        })