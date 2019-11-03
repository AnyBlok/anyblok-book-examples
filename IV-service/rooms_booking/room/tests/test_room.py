# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from datetime import datetime
import time
import pytz


@pytest.mark.usefixtures("rollback_registry")
class TestRoom:
    """ Test python api on AnyBlok models"""

    def test_create_room(self, rollback_registry):
        an_address = rollback_registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!",
        )
        room_count = rollback_registry.Room.query().count()
        room = rollback_registry.Room.insert(name="A1", capacity=25, address=an_address)
        assert rollback_registry.Room.query().count() == room_count + 1
        assert room.name == "A1"

    def test_track_modification_date(self, rollback_registry):
        an_address = rollback_registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!",
        )
        before_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room = rollback_registry.Room.insert(name="A1", capacity=25, address=an_address)
        room.refresh()
        after_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room.name = "A2"
        rollback_registry.flush()
        after_edit = datetime.now(tz=pytz.timezone(time.tzname[0]))
        assert before_create <= room.create_date <= after_create
        assert after_create <= room.edit_date <= after_edit
