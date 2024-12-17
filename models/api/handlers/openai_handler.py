from odoo import models, api
from odoo.exceptions import ValidationError
import requests

class OpenAIHandler(models.AbstractModel):
    _name = 'studio.api.handler.openai'
    _description = 'OpenAI API Handler'

    @api.model
    def send_chat_completion(self, provider_id, messages):
        """Send chat completion request to OpenAI"""
        provider = self.env['studio.api.provider.openai'].browse(provider_id)
        
        payload = provider._prepare_request_payload(messages)
        headers = {
            'Authorization': f'Bearer {provider.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                json=payload,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            
            provider._validate_response(result)
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            raise ValidationError(f'OpenAI API Request failed: {str(e)}')