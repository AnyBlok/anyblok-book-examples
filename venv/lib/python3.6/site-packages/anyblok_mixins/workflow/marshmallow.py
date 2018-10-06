# This file is a part of the AnyBlok project
#
#    Copyright (C) 2018 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import marshmallow  # noqa


def SchemaValidator(schema, get_instance=None):
    def wrap(instance):
        schema.context['registry'] = instance.registry

        if get_instance:
            instance = get_instance(instance)

        schema.load(schema.dump(instance))
        return True

    return wrap
