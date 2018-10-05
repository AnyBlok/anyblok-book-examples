# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

"""Room Blok declaration
"""
from anyblok.blok import Blok


class Room(Blok):
    """Room's Blok class definition
    """
    version = "0.1.0"
    author = "Pierre Verkest"
    required = ['anyblok-core', 'address', 'anyblok-mixins']

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import address  # noqa
        from . import room # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import address  # noqa
        from . import room  # noqa
        reload(address)
        reload(room)

    def update(self, latest_version):
        """Update blok"""
        # if we install this blok in the database we add a new record
        if not latest_version:
            self.install()

    def install(self):
        sorbonne = self.registry.Address.insert(
            first_name="La Sorbonne",
            last_name="La Chancellerie des Universités de Paris",
            street1="47, rue des Écoles ",
            zip_code="75230",
            city="Paris cedex 05",
            country="FRA",
            access="Crie fort pour réveiller le consièrge"
        )
        self.registry.Room.insert(
            name="Salle 101",
            capacity=25,
            address=sorbonne
        )
        self.registry.Room.insert(
            name="Salle 102",
            capacity=30,
            address=sorbonne
        )
        self.registry.Room.insert(
            name="Salle 103",
            capacity=28,
            address=sorbonne
        )
        trinity = self.registry.Address.insert(
            first_name="Trinity College",
            last_name="University of Oxford",
            street1="Broad Street",
            zip_code="OX1 3BH",
            city="Oxford",
            country="GBR",
            access="Ring the bell!"
        )
        self.registry.Room.insert(
            name="Room 101",
            capacity=47,
            address=trinity
        )
        self.registry.Room.insert(
            name="102",
            capacity=50,
            address=trinity
        )
        self.registry.Room.insert(
            name="103",
            capacity=42,
            address=trinity
        )
