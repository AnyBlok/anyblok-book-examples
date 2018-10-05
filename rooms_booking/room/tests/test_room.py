# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from datetime import datetime
import time
import pytz


class TestRoom:
    """Test Room model"""

    def test_create_room(self, rollback_registry):
        registry = rollback_registry
        room_count = registry.Room.query().count()
        room = registry.Room.insert(
            name="A1",
            capacity=25,
        )
        assert registry.Room.query().count() == room_count + 1
        assert room.name == "A1"

    def test_track_modification_date(self, rollback_registry):
        registry = rollback_registry
        before_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room = registry.Room.insert(
            name="A1",
            capacity=25,
        )
        room.refresh()
        after_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        room.name = "A2"
        registry.flush()
        after_edit = datetime.now(tz=pytz.timezone(time.tzname[0]))
        assert before_create <= room.create_date <= after_create
        assert after_create <= room.edit_date <= after_edit
