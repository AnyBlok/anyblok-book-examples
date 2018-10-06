# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.blok import Blok
from anyblok_mixins.release import version
from logging import getLogger
logger = getLogger(__name__)


class AnyBlokMixins(Blok):
    version = version
    author = 'Suzanne Jean-Sébastien'

    @classmethod
    def import_declaration_module(cls):
        from . import readonly  # noqa
        from . import basic  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        from . import readonly
        reload(readonly)
        from . import basic
        reload(basic)
