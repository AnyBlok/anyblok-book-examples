# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from cornice.resource import resource
from anyblok_pyramid_rest_api.crud_resource import CrudResource
from anyblok_pyramid import current_blok


@resource(
    collection_path="/api/v1/addresses",
    path="/api/v1/addresses/{uuid}",
    installed_blok=current_blok(),
)
class AddressesResource(CrudResource):
    model = "Model.Address"
