# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest


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


@pytest.mark.usefixtures('rollback_registry')
class TestApiAddressesBase:
    """ Address test class throught rest api
    """

    def create_address(self, registry):
        """Create a dummy address record"""
        return registry.Address.insert(
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

    def test_addresses_post(self, rollback_registry, webserver):
        """Address POST /api/v1/addresses"""
        response = webserver.post_json('/api/v1/addresses', [_ADDRESS])
        assert response.status_code == 200
        assert response.json_body[0].get('first_name') == 'John'

    def test_addresses_post_fail_empty_body(self, rollback_registry,
                                            webserver):
        """Address POST with empty body /api/v1/addresses"""
        fail = webserver.post_json('/api/v1/addresses', [dict()], status=400)
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'body'

    def test_addresses_post_fail_bad_column(self, rollback_registry,
                                            webserver):
        """Address POST with bad column /api/v1/addresses"""
        address_with_bad_column = _ADDRESS.copy()
        address_with_bad_column['bad_column'] = 'colum_value'
        fail = webserver.post_json('/api/v1/addresses',
                                   [address_with_bad_column], status=400)
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'body'

    def test_addresses_post_fail_bad_value_type(self, rollback_registry,
                                                webserver):
        """Address POST with bad value type /api/v1/addresses"""
        address_with_bad_value_type = _ADDRESS.copy()
        address_with_bad_value_type['first_name'] = 0
        fail = webserver.post_json(
            '/api/v1/addresses',
            address_with_bad_value_type,
            status=400
        )
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'body'

    def test_addresses_get(self, rollback_registry, webserver):
        """Address GET /api/v1/addresses"""
        response = webserver.get('/api/v1/addresses')
        assert response.status_code == 200
        assert len(response.json_body) == 3

    def test_address_get(self, rollback_registry, webserver):
        """Address GET /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        response = webserver.get('/api/v1/addresses/%s' % address.uuid)
        assert response.status_code == 200
        assert response.json_body.get('uuid') == str(address.uuid)

    def test_address_get_fail_bad_path(self, rollback_registry, webserver):
        """Address GET with bad path /api/v1/addresses/x"""
        fail = webserver.get('/api/v1/addresses/x', status=400)
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'path'

    def test_address_put(self, rollback_registry, webserver):
        """Address PUT /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        put_data = _ADDRESS.copy()
        put_data.update(dict(
            first_name='Bob',
            last_name='Plop'
        ))
        response = webserver.put_json(
            '/api/v1/addresses/%s' % address.uuid,
            put_data,
        )
        assert response.status_code == 200
        assert response.json_body.get('uuid') == str(address.uuid)
        assert response.json_body.get('first_name') == 'Bob'
        assert response.json_body.get('last_name') == 'Plop'

    def test_address_put_fail_bad_path(self, rollback_registry, webserver):
        """Address PUT with bad path /api/v1/addresses/{{ uuid }}"""
        put_data = dict(
            first_name='Bob',
        )
        fail = webserver.put_json(
            '/api/v1/addresses/x',
            put_data,
            status=400
        )
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'path'

    def test_address_put_fail_bad_value_type(self, rollback_registry,
                                             webserver):
        """Address PUT with bad value type /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        put_data = dict(
            first_name=0,
        )
        fail = webserver.put_json(
            '/api/v1/addresses/%s' % address.uuid,
            put_data,
            status=400
        )
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'body'

    def test_address_patch(self, rollback_registry, webserver):
        """Address PATCH /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        patch_data = dict(
            first_name='Bob',
            last_name='Plop'
        )
        response = webserver.patch_json(
            '/api/v1/addresses/%s' % address.uuid,
            patch_data,
        )
        assert response.status_code == 200
        assert response.json_body.get('uuid') == str(address.uuid)
        assert response.json_body.get('first_name') == 'Bob'
        assert response.json_body.get('last_name') == 'Plop'

    def test_address_patch_fail_bad_path(self, rollback_registry, webserver):
        """Address PATCH with bad path /api/v1/addresses/x"""
        patch_data = dict(
            first_name='Bob',
        )
        fail = webserver.patch_json(
            '/api/v1/addresses/x',
            patch_data,
            status=400
        )
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'path'

    def test_address_patch_fail_bad_value_type(self, rollback_registry,
                                               webserver):
        """Address PATCH with bad value type /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        patch_data = dict(
            first_name=0,
        )
        fail = webserver.patch_json(
            '/api/v1/addresses/%s' % address.uuid,
            patch_data,
            status=400
        )
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'body'

    def test_address_delete(self, rollback_registry, webserver):
        """Address DELETE /api/v1/addresses/{{ uuid }}"""
        address = self.create_address(rollback_registry)
        response = webserver.delete_json(
            '/api/v1/addresses/%s' % address.uuid,
        )
        assert response.status_code == 200
        assert len(response.json_body) == 0
        assert response.json_body.get('errors') is None

    def test_address_delete_fail_bad_path(self, rollback_registry, webserver):
        """Address DELETE with bad path /api/v1/addresses/x"""
        fail = webserver.patch_json('/api/v1/addresses/x', status=400)
        assert fail.status_code == 400
        assert fail.json_body.get('status') == 'error'
        assert fail.json_body.get('errors')[0].get('location') == 'path'
