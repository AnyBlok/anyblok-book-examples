# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import Integer

Model = Declarations.Model
Mixin = Declarations.Mixin

register = Declarations.register


@register(Model)
class Person:

    @classmethod
    def get_person_types(cls):
        res = super(Person, cls).get_person_types()
        res.update(dict(student="Student"))
        return res


@register(Model.Person)
class Student(Model.Person, Mixin.TrackModel):
    """Student (Polymorphic model that overrides Model.Person)
    """

    PERSON_TYPE = "student"

    id = Integer(
        primary_key=True,
        foreign_key=Model.Person.use('id').options(ondelete="CASCADE")
    )
