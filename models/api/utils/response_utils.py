from typing import Dict, Any, Optional
import json

def parse_response(response_text: str) -> Dict[str, Any]:
    """Parse API response"""
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {'raw_response': response_text}

def extract_error_message(error_response: Dict[str, Any]) -> str:
    """Extract error message from response"""
    if isinstance(error_response, dict):
        return error_response.get('error', {}).get('message', str(error_response))
    return str(error_response)