# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.


class TestUniversity:

    def test_create_university(self, rollback_registry):
        registry = rollback_registry
        university_count = registry.University.query().count()
        university = registry.University.insert(
            name="College 1",
        )

        an_address = registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!",
            university=university,
        )
        assert an_address.university == university
        assert registry.University.query().count() == university_count + 1
        assert university.name == "College 1"

    def test_create_university_with_exinsting_address(
        self, an_address, rollback_registry
    ):
        registry = rollback_registry
        univ = registry.University.insert(
            name="College 2",
        )
        univ.addresses.append(an_address)
