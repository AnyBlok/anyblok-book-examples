# This file is a part of the AnyBlok / Address project
#
#    Copyright (C) 2018 Franck Bret <f.bret@sensee.com>
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2018 Jean-Sebastien Suzanne <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
"""Address model
"""
from anyblok import Declarations
from anyblok.column import String, Country, PhoneNumber, Email

from logging import getLogger

logger = getLogger(__name__)
Model = Declarations.Model
Mixin = Declarations.Mixin


@Declarations.register(Model)
class Address(Mixin.UuidColumn, Mixin.TrackModel, Mixin.BooleanReadOnly):
    """ Postal address
    """

    first_name = String(label="First name", nullable=False)
    last_name = String(label="Last name", nullable=False)
    company_name = String(label="Company name")
    street1 = String(label="Street line 1", nullable=False)
    street2 = String(label="Street line 2")
    street3 = String(label="Street line 3")
    zip_code = String(label="Postal Code")
    state = String(label="State")
    city = String(label="City", nullable=False)
    country = Country(label="Country", nullable=False, mode='alpha_3')
    phone1 = PhoneNumber(label="Phone 1")
    phone2 = PhoneNumber(label="Phone 2")
    email = Email(label="Email")

    def __str__(self):
        return ('{self.uuid}').format(self=self)

    def __repr__(self):
        msg = ('<Address: {self.uuid}, {self.first_name}, {self.last_name}, '
               '{self.company_name}, {self.zip_code}, {self.country} '
               '[RO={self.readonly}] >')

        return msg.format(self=self)
