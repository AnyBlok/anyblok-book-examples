# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

"""Room Blok declaration
"""
from uuid import UUID
from datetime import datetime
from anyblok.blok import Blok
from anyblok_pyramid.adapter import uuid_adapter, datetime_adapter
from pyramid.renderers import JSON


class HttpAPI(Blok):
    """Room Booking Http API's Blok class definition
    """

    version = "0.1.0"
    author = "Pierre Verkest"
    required = ["anyblok-core", "room"]

    @classmethod
    def pyramid_load_config(cls, config):
        """Pyramid http server configuration / initialization
        """
        # include default configuration from packages
        config.include("cornice")

        # Json api renderer
        json_renderer = JSON()
        json_renderer.add_adapter(UUID, uuid_adapter)
        json_renderer.add_adapter(datetime, datetime_adapter)
        config.add_renderer("json", json_renderer)

        # Scan available views
        config.scan(cls.__module__ + ".views")
