# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2019 Franck Bret <franckbret@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

"""Room Blok declaration
"""
import os
from uuid import UUID
from datetime import datetime
from anyblok.blok import Blok
from anyblok_pyramid.adapter import uuid_adapter, datetime_adapter
from pyramid.renderers import JSON


class WebSite(Blok):
    """Room Booking website Blok class definition
    """

    version = "0.1.0"
    author = "Franck Bret"
    required = ["anyblok-core", "room"]

    @classmethod
    def pyramid_load_config(cls, config):
        """Pyramid http server configuration / initialization
        """
        # Pyramid addons
        config.include("pyramid_jinja2")

        # Static resources
        here = os.path.abspath(os.path.dirname(__file__))
        config.add_static_view(
            "/static",
            os.path.realpath(os.path.join(here, "static")),
            cache_max_age=3600,
        )

        # Routes
        config.add_route("index", "/")

        # Scan available views
        config.scan(cls.__module__ + ".views")
