# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.


class TestEmployee:
    """ Test python api on AnyBlok models"""

    def test_create_employee(self, rollback_registry):
        registry = rollback_registry
        employee_count = registry.Person.Employee.query().count()
        employee = registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
            position="unknown",
        )

        assert registry.Person.Employee.query().count() == employee_count + 1
        assert employee.first_name == "John"
        assert employee.last_name == "Doe"
        assert employee.position == "unknown"

    def test_polymorphism(self, rollback_registry):
        registry = rollback_registry
        employee_count = registry.Person.Employee.query().count()
        person_count = registry.Person.query().count()
        registry.Person.insert(
            first_name="John",
            last_name="Doe",
        )
        registry.Person.Employee.insert(
            first_name="John",
            last_name="Doe",
            position="unknown",
        )

        assert registry.Person.query().count() == person_count + 2
        assert registry.Person.Employee.query().count() == employee_count + 1
