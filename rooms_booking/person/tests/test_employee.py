#This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok.tests.testcase import BlokTestCase
from datetime import datetime
import time
import pytz


class TestEmployee(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def setUp(self):
        self.a_person = self.registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
        )

    def test_create_person(self):
        person_count = self.registry.Person.Employee.query().count()
        person = self.registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
        )

        self.assertEqual(
            self.registry.Person.Employee.query().count(),
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

    def test_track_modification_date(self):
        before_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        person = self.registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
        )
        person.refresh()
        after_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        person.name = "John"
        self.registry.flush()
        after_edit = datetime.now(tz=pytz.timezone(time.tzname[0]))
        self.assertTrue(
            before_create <= person.create_date <= after_create
        )
        self.assertTrue(
            after_create <= person.edit_date <= after_edit
        )
