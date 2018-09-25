from anyblok import Declarations
from anyblok.column import String

Model = Declarations.Model
register = Declarations.register


@register(Model)
class Address:

    access = String(label="Access information")
