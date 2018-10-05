# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

"""University Blok declaration
"""


from anyblok.blok import Blok


class University(Blok):
    """University's Blok class definition
    """
    version = "0.1.0"
    author = "Hugo Quezada"
    required = ['anyblok-core', 'address', 'anyblok-mixins', 'person']

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import university  # noqa
        from . import professor  # noqa
        from . import student  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import university  # noqa
        from . import professor  # noqa
        from . import student  # noqa
        reload(university)
        reload(professor)
        reload(student)

    def update(self, latest_version):
        """Update blok"""
        # if we install this blok in the database we add a new record
        if not latest_version:
            self.install()

    def install(self):
        pass
