# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest


@pytest.mark.usefixtures('rollback_registry')
class TestAddress:
    """ Test python api on AnyBlok models"""

    def test_create_address(self, rollback_registry):
        address_count = rollback_registry.Address.query().count()
        queens_college_address = rollback_registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!"
        )
        assert (
            rollback_registry.Address.query().count() ==
            address_count + 1
        )
        assert queens_college_address.access == "Kick the door to open it!"
