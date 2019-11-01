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
from anyblok_marshmallow import SchemaWrapper
from marshmallow import Schema
from anyblok_marshmallow import fields


class RoomNameSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class AddressSchema(SchemaWrapper):
    model = "Model.Address"

    class Schema:
        rooms = fields.List(fields.Nested(RoomNameSchema))


class RoomsSchema(SchemaWrapper):
    model = "Model.Room"

    class Schema:
        address = fields.Nested(AddressSchema)


@resource(
    collection_path='/api/v1/rooms',
    path='/api/v1/rooms/{id}',
    installed_blok=current_blok()
)
class RoomsResource(CrudResource):
    model = "Model.Room"
    default_schema = RoomsSchema
