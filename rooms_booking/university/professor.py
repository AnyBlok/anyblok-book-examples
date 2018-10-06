# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One

Model = Declarations.Model
Mixin = Declarations.Mixin

register = Declarations.register


@register(Model)
class Person:

    @classmethod
    def get_person_types(cls):
        res = super(Person, cls).get_person_types()
        res.update(dict(PROFESSOR="Professor"))
        return res


@register(Model.Person.Employee)
class Professor(Model.Person.Employee, Mixin.TrackModel):
    """Professor (Polymorphic model that overrides Model.Person.Employee)
    """

    PERSON_TYPE="PROFESSOR"

    id = Integer(primary_key=True,
                 foreign_key=Model.Person.Employee.use('id').options(
                    ondelete="CASCADE"))

