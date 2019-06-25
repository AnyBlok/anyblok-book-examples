# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.


class TestPerson:
    """ Test python api on AnyBlok models"""

    def test_create_person(self, rollback_registry):
        registry = rollback_registry
        person_count = registry.Person.query().count()
        person = registry.Person.insert(
            first_name="John",
            last_name="Doe",
        )

        assert registry.Person.query().count() == person_count + 1
        assert person.first_name == "John"
        assert person.last_name == "Doe"
