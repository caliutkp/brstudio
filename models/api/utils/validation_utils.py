from typing import Dict, Any, List
from odoo.exceptions import ValidationError

def validate_required_fields(data: Dict[str, Any], required: List[str]) -> None:
    """Validate required fields"""
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")

def validate_api_key(api_key: str) -> None:
    """Validate API key format"""
    if not api_key or len(api_key) < 8:
        raise ValidationError("Invalid API key format")