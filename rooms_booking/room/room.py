# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
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
class Room(Mixin.IdColumn, Mixin.TrackModel):

    name = String(label="Room name", nullable=False, index=True)
    capacity = Integer(label="Capacity", nullable=False)
    address = Many2One(
        label="Address", model=Model.Address, nullable=False, one2many="rooms"
    )
