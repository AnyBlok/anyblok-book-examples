# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok.tests.testcase import BlokTestCase


class TestUniversity(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def setUp(self):
        self.an_address = self.registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!"
        )

    def test_create_university(self):
        university_count = self.registry.University.query().count()
        university = self.registry.University.insert(
            name="College 1",
        )

        self.an_address = self.registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!",
            university=university,
        )

        self.assertEqual(
            self.registry.University.query().count(),
            university_count + 1
        )
        self.assertEqual(
            university.name,
            "College 1"
        )

    def test_create_university_with_exinsting_address(self):
        univ = self.registry.University.insert(
            name="College 2",
        )
        univ.addresses.append(self.an_address)
