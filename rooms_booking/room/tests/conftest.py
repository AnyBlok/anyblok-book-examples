import pytest
from anyblok.conftest import *  # noqa: F401,F403


@pytest.fixture()
def an_address(rollback_registry):
    return rollback_registry.Address.insert(
        first_name="The Queen's College",
        last_name="University of oxford",
        street1="High Street",
        zip_code="OX1 4AW",
        city="Oxford",
        country="GBR",
        access="Kick the door to open it!"
    )
