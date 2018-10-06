# This file is a part of the AnyBlok / book examples project
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
            address=self.an_address
        )

        self.assertEqual(
            self.registry.University.query().count(),
            university_count + 1
        )
        self.assertEqual(
            university.name,
            "College 1"
        )

    def test_track_modification_date(self):
        before_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        university = self.registry.University.insert(
            name="College 1",
        )
        university.refresh()
        after_create = datetime.now(tz=pytz.timezone(time.tzname[0]))
        university.name = "College 1"
        self.registry.flush()
        after_edit = datetime.now(tz=pytz.timezone(time.tzname[0]))
        self.assertTrue(
            before_create <= university.create_date <= after_create
        )
        self.assertTrue(
            after_create <= university.edit_date <= after_edit
        )
