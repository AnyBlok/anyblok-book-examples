# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok.tests.testcase import BlokTestCase


class TestEmployee(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_employee(self):
        employee_count = self.registry.Person.Employee.query().count()
        employee = self.registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
            position="unknown",
        )

        self.assertEqual(
            self.registry.Person.Employee.query().count(),
            employee_count + 1
        )
        self.assertEqual(
            employee.first_name,
            "John"
        )
        self.assertEqual(
            employee.last_name,
            "Doe"
        )
        self.assertEqual(
            employee.position,
            "unknown"
        )

    def test_polymorphism(self):

        employee_count = self.registry.Person.Employee.query().count()
        person_count = self.registry.Person.query().count()
        self.registry.Person.insert(
            first_name="John",
            last_name="Doe",
        )
        self.registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
            position="unknown",
        )

        self.assertEqual(
            self.registry.Person.query().count(),
            person_count + 2
        )
        self.assertEqual(
            self.registry.Person.Employee.query().count(),
            employee_count + 1
        )
