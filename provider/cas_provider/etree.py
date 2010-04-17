# Import etree from anywhere
try:
    # lxml http://codespeak.net/lxml/
    from lxml import etree
    
    # Define register_namespace function and ElementRoot for proper serialization
    NSMAP = {}
    def register_namespace(prefix, uri):
        NSMAP[prefix] = uri
    
    def ElementRoot(*args, **kwargs):
        kwargs['nsmap'] = NSMAP
        return etree.Element(*args, **kwargs)

except ImportError:
    try:
        # normal cElementTree install
        import cElementTree as etree
    except ImportError:
        # normal ElementTree install
        import elementtree.ElementTree as etree

    try:
        register_namespace = etree.register_namespace
    except AttributeError:
        def register_namespace(prefix, uri):
            etree._namespace_map[uri] = prefix

    def ElementRoot(*args, **kwargs):
        return etree.Element(*args, **kwargs)

__all__ = ('etree', 'register_namespace', 'ElementRoot')
