import re
from typing import Any, Dict, List, Optional

def validate_identifier(name: str) -> bool:
    """Validate Python identifier rules"""
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))

def merge_dicts(*dicts: Dict) -> Dict:
    """Merge multiple dictionaries"""
    result = {}
    for d in dicts:
        result.update(d)
    return result

def filter_none_values(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove None values from dictionary"""
    return {k: v for k, v in data.items() if v is not None}

def ensure_list(value: Any) -> List:
    """Ensure value is a list"""
    if value is None:
        return []
    return value if isinstance(value, list) else [value]