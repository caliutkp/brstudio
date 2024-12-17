from typing import Dict, Any, Optional
import json

def prepare_request_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Prepare request data"""
    return {k: v for k, v in data.items() if v is not None}

def format_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """Format API response"""
    return {
        'success': True,
        'data': response,
        'error': None
    }

def format_error(error: Exception) -> Dict[str, Any]:
    """Format API error"""
    return {
        'success': False,
        'data': None,
        'error': str(error)
    }