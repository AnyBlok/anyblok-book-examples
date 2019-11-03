# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from pyramid.view import view_config
from anyblok_pyramid import current_blok


@view_config(
    route_name="index",
    installed_blok=current_blok(),
    renderer="../templates/index.jinja2",
)
def route_index(request):
    """No authentication required, html rendering is done through jinja2 templates
    """
    registry = request.anyblok.registry
    rooms = registry.Room.query().all()
    return dict(message="Bienvenue", rooms=rooms)
