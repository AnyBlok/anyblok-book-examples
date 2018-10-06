# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok_pyramid.tests.testcase import PyramidBlokTestCase


_ADDRESS = dict(
    first_name="John",
    last_name="Doe",
    street1="1 street",
    street2="crossroad",
    street3="♥",
    zip_code="99999",
    state="A region",
    city="Nowhere",
    country="FRA"
)


class TestApiAddressesBase(PyramidBlokTestCase):
    """ Address test class throught rest api
    """

    def create_address(self):
        """Create a dummy address record"""
        address = self.registry.Address.insert(
            first_name="John",
            last_name="Doe",
            street1="1 street",
            street2="crossroad",
            street3="♥",
            zip_code="99999",
            state="A region",
            city="Nowhere",
            country="FRA"
        )
        return address

    def test_addresses_post(self):
        """Address POST /api/v1/addresses"""
        response = self.webserver.post_json(
            '/api/v1/addresses',
            _ADDRESS,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body.get('first_name'), 'John')

    def test_addresses_post_fail_empty_body(self):
        """Address POST with empty body /api/v1/addresses"""
        fail = self.webserver.post_json(
            '/api/v1/addresses',
            dict(),
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'body')

    def test_addresses_post_fail_bad_column(self):
        """Address POST with bad column /api/v1/addresses"""
        address_with_bad_column = _ADDRESS.copy()
        address_with_bad_column['bad_column'] = 'colum_value'
        fail = self.webserver.post_json(
            '/api/v1/addresses',
            address_with_bad_column,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'body')

    def test_addresses_post_fail_bad_value_type(self):
        """Address POST with bad value type /api/v1/addresses"""
        address_with_bad_value_type = _ADDRESS.copy()
        address_with_bad_value_type['first_name'] = 0
        fail = self.webserver.post_json(
            '/api/v1/addresses',
            address_with_bad_value_type,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'body')

    def test_addresses_get(self):
        """Address GET /api/v1/addresses"""
        address = self.create_address()
        response = self.webserver.get(
            '/api/v1/addresses',
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json_body), 1)
        self.assertEqual(response.json_body[0].get('uuid'), str(address.uuid))

    def test_address_get(self):
        """Address GET /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        response = self.webserver.get(
            '/api/v1/addresses/%s' % address.uuid,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body.get('uuid'), str(address.uuid))

    def test_address_get_fail_bad_path(self):
        """Address GET with bad path /api/v1/addresses/x"""
        fail = self.webserver.get(
            '/api/v1/addresses/x',
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'path')

    def test_address_put(self):
        """Address PUT /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        put_data = _ADDRESS.copy()
        put_data.update(dict(
            first_name='Bob',
            last_name='Plop'
        ))
        response = self.webserver.put_json(
            '/api/v1/addresses/%s' % address.uuid,
            put_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body.get('uuid'), str(address.uuid))
        self.assertEqual(response.json_body.get('first_name'), 'Bob')
        self.assertEqual(response.json_body.get('last_name'), 'Plop')

    def test_address_put_fail_bad_path(self):
        """Address PUT with bad path /api/v1/addresses/{{ uuid }}"""
        put_data = dict(
            first_name='Bob',
        )
        fail = self.webserver.put_json(
            '/api/v1/addresses/x',
            put_data,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'path')

    def test_address_put_fail_bad_value_type(self):
        """Address PUT with bad value type /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        put_data = dict(
            first_name=0,
        )
        fail = self.webserver.put_json(
            '/api/v1/addresses/%s' % address.uuid,
            put_data,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'body')

    def test_address_patch(self):
        """Address PATCH /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        patch_data = dict(
            first_name='Bob',
            last_name='Plop'
        )
        response = self.webserver.patch_json(
            '/api/v1/addresses/%s' % address.uuid,
            patch_data,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json_body.get('uuid'), str(address.uuid))
        self.assertEqual(response.json_body.get('first_name'), 'Bob')
        self.assertEqual(response.json_body.get('last_name'), 'Plop')

    def test_address_patch_fail_bad_path(self):
        """Address PATCH with bad path /api/v1/addresses/x"""
        patch_data = dict(
            first_name='Bob',
        )
        fail = self.webserver.patch_json(
            '/api/v1/addresses/x',
            patch_data,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'path')

    def test_address_patch_fail_bad_value_type(self):
        """Address PATCH with bad value type /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        patch_data = dict(
            first_name=0,
        )
        fail = self.webserver.patch_json(
            '/api/v1/addresses/%s' % address.uuid,
            patch_data,
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'body')

    def test_address_delete(self):
        """Address DELETE /api/v1/addresses/{{ uuid }}"""
        address = self.create_address()
        response = self.webserver.delete_json(
            '/api/v1/addresses/%s' % address.uuid,
            headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json_body), 0)
        self.assertIsNone(response.json_body.get('errors'), None)

    def test_address_delete_fail_bad_path(self):
        """Address DELETE with bad path /api/v1/addresses/x"""
        fail = self.webserver.patch_json(
            '/api/v1/addresses/x',
            headers=self.headers,
            status=400
        )
        self.assertEqual(fail.status_code, 400)
        self.assertEqual(fail.json_body.get('status'), 'error')
        self.assertEqual(
            fail.json_body.get('errors')[0].get('location'), 'path')
