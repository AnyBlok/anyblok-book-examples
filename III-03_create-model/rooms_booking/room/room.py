# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok import Declarations
from anyblok.column import String, Integer

Model = Declarations.Model
register = Declarations.register


@register(Model)
class Room:

    id = Integer(primary_key=True)
    name = String(label="Room name", nullable=False, index=True)
    capacity = Integer(label="Capacity", nullable=False)
