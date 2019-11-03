# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

import time
import pytz
from datetime import datetime


class TestRoom:
    """Test Room model"""

    def test_create_room(self, rollback_registry, an_address):
        registry = rollback_registry
        room_count = registry.Room.query().count()
        room = registry.Room.insert(
            name="A1",
            capacity=25,
            address=an_address
        )
        assert registry.Room.query().count() == room_count + 1
        assert room.name == "A1"

    def test_track_modification_date(self, rollback_registry, an_address):
        registry = rollback_registry
        before_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room = registry.Room.insert(
            name="A1",
            capacity=25,
            address=an_address
        )
        room.refresh()
        after_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room.name = "A2"
        registry.flush()
        after_edit = datetime.now(tz=pytz.timezone(time.tzname[0]))
        assert before_create <= room.create_date <= after_create
        assert after_create <= room.edit_date <= after_edit

    def test_change_addresses(self, rollback_registry, an_address):
        registry = rollback_registry
        an_other_address = registry.Address.insert(
            first_name="Campus de Carcassonne",
            last_name="Université de Perpignan",
            street1="Statistique et Traitement Informatique des Données",
            street2="2535 Route de Saint-Hilaire",
            zip_code="11000",
            city="Carcassonne",
            country="FRA",
            access="Kick the door to open it!"
        )
        roomA2 = registry.Room.insert(
            name="A2",
            capacity=32,
            address=an_address,
        )
        roomA3 = registry.Room.insert(
            name="A3",
            capacity=32,
            address=an_address,
        )
        an_other_address.rooms.extend([roomA2, roomA3])
        assert len(an_other_address.rooms) == 2
        assert len(an_address.rooms) == 0
