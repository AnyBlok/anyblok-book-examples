# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from pyramid.view import view_config
from anyblok_pyramid import current_blok
from rooms_booking.room.schemas import RoomsSchema


@view_config(
    route_name="index",
    installed_blok=current_blok(),
    renderer="../templates/index.jinja2",
)
def route_index(request):
    """Website homepage.
    No authentication required, html rendering is done through jinja2 templates
    """
    registry = request.anyblok.registry
    # Instantiate a schema for data serialization. Exclude the fields we don't
    # want to be exposed on template side
    rooms_schema = RoomsSchema(
        registry=registry,
        many=True,
        only=("name", "capacity", "address.first_name", "address.last_name"),
    )
    # Query our records
    rooms = registry.Room.query().all()
    # Serialize rooms records
    rooms_data = rooms_schema.dump(rooms)
    # Expose our data to html template (jinja2)
    return dict(title="Bienvenue", rooms=rooms_data)
