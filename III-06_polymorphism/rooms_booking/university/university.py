# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import String
from anyblok.relationship import Many2One

Model = Declarations.Model
Mixin = Declarations.Mixin

register = Declarations.register


@register(Model)
class University(Mixin.IdColumn):

    name = String(label="University name", nullable=False, index=True)


@register(Model)
class Address:

    university = Many2One(
        label="University",
        model=Model.University,
        nullable=True,
        one2many="addresses",
    )
