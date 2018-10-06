# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
"""Basic mixins
"""
from datetime import datetime
from uuid import uuid4

from anyblok import Declarations
from anyblok.column import Integer, DateTime, UUID


Mixin = Declarations.Mixin


@Declarations.register(Mixin)
class IdColumn:
    """ `ìd` primary key mixin
    """
    id = Integer(primary_key=True)


@Declarations.register(Mixin)
class UuidColumn:
    """ `UUID` id primary key mixin
    """
    uuid = UUID(primary_key=True, default=uuid4, binary=False)


@Declarations.register(Mixin)
class TrackModel:
    """ A mixin to store record creation and edition date
    """
    create_date = DateTime(default=datetime.now, nullable=False)
    edit_date = DateTime(default=datetime.now, nullable=False,
                         auto_update=True)
