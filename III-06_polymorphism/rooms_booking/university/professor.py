# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import Integer, Selection

Model = Declarations.Model

register = Declarations.register


@register(Model)
class Person:

    @classmethod
    def get_person_types(cls):
        res = super(Person, cls).get_person_types()
        res.update(dict(professor="Professor"))
        return res


@register(Model.Person.Employee)
class Professor(Model.Person.Employee):
    """Professor (Polymorphic model that overrides Model.Person.Employee)
    """

    PERSON_TYPE = "professor"

    id = Integer(
        primary_key=True,
        foreign_key=Model.Person.Employee.use('id').options(ondelete="CASCADE")
    )
    qualification = Selection(
        selections=dict(
            doctorate='Doctorate',
            master='Master',
            bachelor='B achelor',
        ),
        nullable=False
    )
