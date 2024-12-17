import re
from typing import Dict, Any

def validate_field_config(config: Dict[str, Any]) -> Dict[str, str]:
    """Validate field configuration and return errors if any"""
    errors = {}
    
    if not _is_valid_name(config.get('name', '')):
        errors['name'] = 'Invalid field name format'
    
    if not _is_valid_type(config.get('field_type', '')):
        errors['field_type'] = 'Invalid field type'
    
    return errors

def _is_valid_name(name: str) -> bool:
    """Check if field name follows Python identifier rules"""
    if not name:
        return False
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

def _is_valid_type(field_type: str) -> bool:
    """Check if field type is supported"""
    valid_types = {'char', 'integer', 'float', 'date', 'datetime', 
                  'boolean', 'many2one', 'one2many', 'many2many'}
    return field_type in valid_types