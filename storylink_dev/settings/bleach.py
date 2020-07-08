#configuracion django-bleach

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'ul', 'li' 'ol', 'em', 'strong', 'span', 's', 'br']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['style']

# Which CSS properties are allowed in 'style' attributes (assuming style is
# an allowed attribute)
BLEACH_ALLOWED_STYLES = ['text-decoration', 'text-align']

# Which protocols (and pseudo-protocols) are allowed in 'src' attributes
# (assuming src is an allowed attribute)
BLEACH_ALLOWED_PROTOCOLS = []

# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = False

# Strip HTML comments, or leave them in.
BLEACH_STRIP_COMMENTS = False

BLEACH_DEFAULT_WIDGET = 'ckeditor.widgets.CKEditorWidget'