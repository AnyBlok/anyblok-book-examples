# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok.tests.testcase import BlokTestCase


class TestPerson(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_person(self):
        person_count = self.registry.Person.query().count()
        person = self.registry.Person.insert(
            first_name="John",
            last_name="Doe",
        )

        self.assertEqual(
            self.registry.Person.query().count(),
            person_count + 1
        )
        self.assertEqual(
            person.first_name,
            "John"
        )
        self.assertEqual(
            person.last_name,
            "Doe"
        )
