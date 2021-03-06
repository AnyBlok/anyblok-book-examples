# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.


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
