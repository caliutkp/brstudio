from lxml import etree

def generate_view_arch(components):
    """Generate view architecture from components"""
    root = etree.Element('form')
    _build_component_tree(root, components)
    return etree.tostring(root, pretty_print=True)

def _build_component_tree(parent, components):
    """Recursively build component tree"""
    for component in sorted(components, key=lambda c: c.sequence):
        element = etree.SubElement(parent, component.component_type)
        if component.attrs:
            _set_attributes(element, component.attrs)
        if component.child_ids:
            _build_component_tree(element, component.child_ids)

def _set_attributes(element, attrs_string):
    """Set element attributes from string"""
    try:
        attrs = eval(attrs_string)
        for key, value in attrs.items():
            element.set(key, str(value))
    except Exception:
        pass