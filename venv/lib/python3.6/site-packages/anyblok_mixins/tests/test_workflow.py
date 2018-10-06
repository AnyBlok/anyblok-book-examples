# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import DBTestCase
from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok_mixins.mixins.exceptions import (
    ForbidDeleteException, ForbidUpdateException
)
from anyblok_mixins.workflow.exceptions import WorkFlowException
from sqlalchemy.exc import StatementError
from unittest import skipIf

register = Declarations.register
unregister = Declarations.unregister
Mixin = Declarations.Mixin
Model = Declarations.Model

try:
    from anyblok_mixins.workflow.marshmallow import SchemaValidator
    has_marshmallow = True
except ImportError as e:
    has_marshmallow = False


class TestWorkFlow(DBTestCase):

    def init_registry(self, func):
        return self.init_registry_with_bloks(('anyblok-workflow',), func)

    def test_empty_workflow(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):
                id = Integer(primary_key=True)

        with self.assertRaises(WorkFlowException):
            self.init_registry(add_in_registry)

    def test_simple_workflow_without_default_value(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        with self.assertRaises(StatementError):
            registry.Test.insert()

    def test_simple_workflow_with_default_value(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        self.assertEqual(test.state, 'draft')

    def test_simple_workflow_with_two_default_value(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True},
                    'done': {'default': True},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        with self.assertRaises(StatementError):
            registry.Test.insert()

    def test_simple_workflow_without_allowed_to(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            registry.flush()

    def test_simple_workflow_with_unwanted_allowed_to(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['another']},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            registry.flush()

    def test_simple_workflow_with_allowed_to(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['done']},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        registry.flush()

    def test_simple_workflow_with_allowed_to_2(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': {'done': True}},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        registry.flush()

    def test_simple_workflow_with_allowed_to_3(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': {'done': False}},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            registry.flush()

    def test_simple_workflow_with_allowed_to_4(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': {'done': 'allowed_to_done'}},
                    'done': {},
                }
                id = Integer(primary_key=True)

                def allowed_to_done(self):
                    return True

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        registry.flush()

    def test_simple_workflow_with_allowed_to_5(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': {'done': 'forbidden_to_done'}},
                    'done': {},
                }
                id = Integer(primary_key=True)

                def forbidden_to_done(self):
                    return False

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            registry.flush()

    def test_simple_workflow_with_allowed_to_6(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': {'done': ['allowed_to_done']}},
                    'done': {},
                }
                id = Integer(primary_key=True)

                def allowed_to_done(self):
                    return True

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        registry.flush()

    def test_simple_workflow_with_allowed_to_7(self):

        def add_in_registry():

            def allowed_to_done(instance):
                return True

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': {'done': allowed_to_done}},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        registry.flush()

    def test_simple_workflow_with_allowed_to_8(self):

        def add_in_registry():

            def forbidden_to_done(self):
                return False

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': {'done': forbidden_to_done}},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            registry.flush()

    def test_simple_workflow_without_allowed_to_with_method(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        with self.assertRaises(WorkFlowException):
            test.state_to('done')

    def test_simple_workflow_with_unwanted_allowed_to_with_method(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['another']},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state = 'done'
        with self.assertRaises(WorkFlowException):
            test.state_to('done')

    def test_simple_workflow_with_allowed_to_with_method(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['done']},
                    'done': {},
                }
                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')

    def test_simple_workflow_change_state_with_apply_change_1(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['done']},
                    'done': {'apply_change': 'changed_state_from'},
                }
                id = Integer(primary_key=True)
                name = String()

                def changed_state_from(self, from_state):
                    self.name = 'changed'

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        self.assertNotEqual(test.name, 'changed')
        test.state_to('done')
        self.assertEqual(test.name, 'changed')

    def test_simple_workflow_change_state_with_apply_change_2(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True, 'allowed_to': ['done']},
                    'done': {'apply_change': {'draft': 'changed_state_from'}},
                }
                id = Integer(primary_key=True)
                name = String()

                def changed_state_from(self, from_state):
                    self.name = 'changed'

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        self.assertNotEqual(test.name, 'changed')
        test.state_to('done')
        self.assertEqual(test.name, 'changed')

    def test_simple_workflow_validators(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': 'allowed_to_done'},
                }
                id = Integer(primary_key=True)
                name = String()

                def allowed_to_done(self):
                    return True

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        self.registry.flush()

    def test_simple_workflow_validators_2(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': 'allowed_to_done'},
                }
                id = Integer(primary_key=True)
                name = String()

                def allowed_to_done(self):
                    return self.name != 'changed'

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        with self.assertRaises(WorkFlowException):
            self.registry.flush()

    def test_simple_workflow_validators_3(self):

        def add_in_registry():

            def allowed_to_done(self):
                return True

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': allowed_to_done},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        self.registry.flush()

    def test_simple_workflow_validators_4(self):

        def add_in_registry():

            def allowed_to_done(self):
                return self.name != 'changed'

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': allowed_to_done},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        with self.assertRaises(WorkFlowException):
            self.registry.flush()

    def test_simple_workflow_validators_5(self):

        def add_in_registry():

            def allowed_to_done(self):
                return True

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': [allowed_to_done]},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        self.registry.flush()

    def test_simple_workflow_readonly(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'readonly': True},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.name = 'changed'
        with self.assertRaises(ForbidUpdateException):
            self.registry.flush()

    def test_simple_workflow_readonly_2(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'readonly': True,
                             'apply_change': {
                                 'draft': 'changed_state_from_draft'}},
                }
                id = Integer(primary_key=True)
                name = String()

                def changed_state_from_draft(self, previous_values):
                    self.name = 'changed'

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        self.assertNotEqual(test.name, 'changed')
        test.state_to('done')
        self.assertEqual(test.name, 'changed')
        self.registry.flush()

    def test_simple_workflow_readonly_is_not_deletable(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'readonly': True},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        with self.assertRaises(ForbidDeleteException):
            test.delete()

    def test_simple_workflow_readonly_is_deletable(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'readonly': True, 'deletable': True},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.delete()

    def test_simple_workflow_is_not_deletable(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'deletable': False},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        with self.assertRaises(ForbidDeleteException):
            test.delete()

    def test_simple_workflow_is_deletable(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        test.delete()

    @skipIf(not has_marshmallow, "marshmallow is not installed")
    def test_schema_validator(self):

        from marshmallow import Schema, fields

        class MySchema(Schema):
            id = fields.Integer(required=True)
            state = fields.String(required=True)
            name = fields.String()

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': SchemaValidator(MySchema())},
                }
                id = Integer(primary_key=True)
                name = String(default='')

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        test.state_to('done')
        self.registry.flush()

    @skipIf(not has_marshmallow, "marshmallow is not installed")
    def test_schema_validator_2(self):

        from marshmallow import Schema, fields, exceptions

        class MySchema(Schema):
            id = fields.Integer(required=True)
            state = fields.String(required=True)
            name = fields.String(required=True)

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': SchemaValidator(MySchema())},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        with self.assertRaises(exceptions.ValidationError):
            test.state_to('done')

    @skipIf(not has_marshmallow, "marshmallow is not installed")
    def test_schema_validator_3(self):

        from marshmallow import Schema, fields, exceptions

        class MySchema(Schema):
            id = fields.Integer(required=True)
            state = fields.String(required=True)
            name = fields.String(required=True)

        def add_in_registry():

            @register(Model)
            class Test(Mixin.WorkFlow):

                WORKFLOW = {
                    'draft': {'default': True,
                              'allowed_to': ['done']},
                    'done': {'validators': SchemaValidator(
                        MySchema(), get_instance=lambda x: x)},
                }
                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        test = registry.Test.insert()
        with self.assertRaises(exceptions.ValidationError):
            test.state_to('done')
