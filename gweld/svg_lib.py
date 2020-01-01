from lxml import etree

def root_tag(width, height):
    return etree.Element('svg', {'width': str(width), 'height': str(height), 'xmlns': 'http://www.w3.org/2000/svg'})

def add_tag(parent, tag, attributes=None, text=None):
    tag = etree.SubElement(parent, tag, attributes)
    tag.text = text
    return tag 

def add_text(parent, pos, text, style):
    add_tag(parent, 'text', attributes={
        'x': str(pos[0]),
        'y': str(pos[1]),
        'transform': f'rotate({style.angle} {pos[0]} {pos[1]})',
        'class': f'{style.text_type}_label'
    }, text=text)

def to_string(tree):
    return etree.tostring(tree, pretty_print=True)
