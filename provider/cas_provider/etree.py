# lxml http://codespeak.net/lxml/
from lxml import etree

# Define register_namespace function and ElementRoot for proper serialization
NSMAP = {}


def register_namespace(prefix, uri):
    NSMAP[prefix] = uri


def ElementRoot(*args, **kwargs):
    kwargs['nsmap'] = NSMAP
    return etree.Element(*args, **kwargs)

__all__ = ('etree', 'register_namespace', 'ElementRoot')
