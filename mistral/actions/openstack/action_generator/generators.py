# Copyright 2014 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistral.actions.openstack.action_generator import base
from mistral.actions.openstack import actions


class NovaActionGenerator(base.OpenStackActionGenerator):
    _action_namespace = "nova"
    base_action_class = actions.NovaAction


class GlanceActionGenerator(base.OpenStackActionGenerator):
    _action_namespace = "glance"
    base_action_class = actions.GlanceAction


class KeystoneActionGenerator(base.OpenStackActionGenerator):
    _action_namespace = "keystone"
    base_action_class = actions.KeystoneAction
