from .settings import * 

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    mimetypes.add_type("text/css", ".css", True)