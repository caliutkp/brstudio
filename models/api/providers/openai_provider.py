from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpenAIProvider(models.Model):
    _name = 'studio.api.provider.openai'
    _inherit = ['studio.api.provider']
    _description = 'OpenAI API Provider'

    model = fields.Selection([
        ('gpt-4', 'GPT-4'),
        ('gpt-3.5-turbo', 'GPT-3.5 Turbo'),
    ], string='Model', required=True, default='gpt-4')
    
    max_tokens = fields.Integer(string='Max Tokens', default=2048)
    temperature = fields.Float(string='Temperature', default=0.7)
    
    def _prepare_request_payload(self, messages):
        """Prepare OpenAI API request payload"""
        return {
            'model': self.model,
            'messages': messages,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
        }
    
    def _validate_response(self, response):
        """Validate OpenAI API response"""
        if response.get('error'):
            raise ValidationError(f"OpenAI API Error: {response['error'].get('message')}")
        return True