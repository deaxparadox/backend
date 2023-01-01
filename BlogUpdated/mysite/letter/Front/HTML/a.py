from .attributes import Common, IsNone


def ReturnAttr(k,v):
    return f" {k}={repr(v)}"

def a(text,**Aargs):
    keys = Aargs.keys()
    attrs = str()
    for k in keys:
        value = Aargs.get(k)
        if value is not None:
            attrs += ReturnAttr(k.lower(), value)
            
    return f"<a{attrs}>{text}</a>"
