# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2019 Franck Bret <franckbret@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest


@pytest.mark.usefixtures("rollback_registry")
class TestWebSite:
    """ Test website Pyramid views
    """

    def test_index(self, webserver):
        response = webserver.get("/")
        assert response.status_code == 200
        assert response.content_type == "text/html"

    def test_logo(self, webserver):
        response = webserver.get("/static/img/logo.png")
        assert response.status_code == 200
        assert response.content_type == "image/png"

    def test_css(self, webserver):
        response = webserver.get("/static/css/styles.css")
        assert response.status_code == 200
        assert response.content_type == "text/css"

    def test_index_content(self, rollback_registry, webserver):
        response = webserver.get("/")
        assert (
            response.html.find_all("title")[0].get_text()
            == response.html.find_all("h1")[0].get_text()
            == "Bienvenue"
        )
        assert (
            len(response.html.find_all("li"))
            == rollback_registry.Room.query().count()
        )
