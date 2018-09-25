from anyblok.tests.testcase import BlokTestCase


class TestAddress(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_address(self):
        queens_college_address = self.registry.Address.insert(
            first_name="The Queen's College",
            last_name="University of oxford",
            street1="High Street",
            zip_code="OX1 4AW",
            city="Oxford",
            country="GBR",
            access="Kick the door to open it!"
        )
        self.assertEqual(self.registry.Address.query().count(), 2)
        self.assertEqual(
            queens_college_address.access,
            "Kick the door to open it!"
        )
