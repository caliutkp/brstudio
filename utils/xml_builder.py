from lxml import etree
from typing import Dict, List, Optional

class XMLBuilder:
    """Helper class for building XML structures"""
    
    @staticmethod
    def create_element(tag: str, attributes: Optional[Dict] = None, text: Optional[str] = None) -> etree.Element:
        """Create XML element with attributes and text"""
        elem = etree.Element(tag)
        if attributes:
            for key, value in attributes.items():
                elem.set(key, str(value))
        if text:
            elem.text = text
        return elem
    
    @staticmethod
    def add_children(parent: etree.Element, children: List[etree.Element]) -> None:
        """Add child elements to parent"""
        for child in children:
            parent.append(child)
    
    @staticmethod
    def to_string(elem: etree.Element, pretty_print: bool = True) -> str:
        """Convert element to string"""
        return etree.tostring(elem, pretty_print=pretty_print, encoding='unicode')