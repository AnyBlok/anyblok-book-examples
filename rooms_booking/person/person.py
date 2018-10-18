# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo QUEZADA <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import String, Selection

Model = Declarations.Model
Mixin = Declarations.Mixin

register = Declarations.register


@register(Model)
class Person(Mixin.IdColumn):
    PERSON_TYPE = 'person'

    first_name = String(label="Person name", nullable=False, index=True)
    last_name = String(label="Person name", nullable=False, index=True)
    person_type = Selection(selections='get_person_types', nullable=False)

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Person, cls).define_mapper_args()
        if cls.__registry_name__ == 'Model.Person':
            mapper_args.update({'polymorphic_on': cls.person_type})

        mapper_args.update({'polymorphic_identity': cls.PERSON_TYPE})
        return mapper_args

    @classmethod
    def query(cls, *args, **kwargs):
        query = super(Person, cls).query(*args, **kwargs)
        if cls.__registry_name__.startswith('Model.Person.'):
            query = query.filter(cls.person_type == cls.PERSON_TYPE)
        return query

    @classmethod
    def get_person_types(cls):
        return dict(person='Person', )
