# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2019 Franck Bret <franckbret@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
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
