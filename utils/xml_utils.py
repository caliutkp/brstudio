from lxml import etree
from typing import Dict, List, Optional

def create_view_xml(view_type: str, fields: List[Dict], options: Optional[Dict] = None) -> str:
    """Create XML architecture for view"""
    root = etree.Element(view_type)
    
    if view_type == 'form':
        sheet = etree.SubElement(root, 'sheet')
        _add_form_elements(sheet, fields, options)
    elif view_type == 'tree':
        _add_tree_elements(root, fields, options)
    
    return etree.tostring(root, pretty_print=True, encoding='unicode')

def _add_form_elements(parent: etree.Element, fields: List[Dict], options: Optional[Dict]):
    """Add elements to form view"""
    if options and options.get('use_groups', True):
        group = etree.SubElement(parent, 'group')
        for field in fields:
            field_elem = etree.SubElement(group, 'field')
            field_elem.set('name', field['name'])
            if field.get('required'):
                field_elem.set('required', '1')
    else:
        for field in fields:
            field_elem = etree.SubElement(parent, 'field')
            field_elem.set('name', field['name'])

def _add_tree_elements(parent: etree.Element, fields: List[Dict], options: Optional[Dict]):
    """Add elements to tree view"""
    for field in fields:
        field_elem = etree.SubElement(parent, 'field')
        field_elem.set('name', field['name'])