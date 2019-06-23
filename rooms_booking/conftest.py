# This file is a part of the AnyBlok project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2018 Denis VIVIÈS <dvivies@geoblink.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest
from anyblok.conftest import *  # noqa


# Pyramid
from webtest import TestApp
from anyblok_pyramid.pyramid_config import Configurator


@pytest.fixture(scope="session")
def webserver(request, init_session):
    config = Configurator()
    config.include_from_entry_point()
    # No param here # for includeme in self.includemes:
    # No param here #     config.include(includeme)

    config.load_config_bloks()
    app = config.make_wsgi_app()
    return TestApp(app)
