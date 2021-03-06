# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from marconi.storage import sqlite
from marconi.storage.sqlite import controllers
from marconi.tests.storage import base


class SQliteQueueTests(base.QueueControllerTest):
    driver_class = sqlite.Driver
    controller_class = controllers.QueueController


class SQliteMessageTests(base.MessageControllerTest):
    driver_class = sqlite.Driver
    controller_class = controllers.MessageController


class SQliteClaimTests(base.ClaimControllerTest):
    driver_class = sqlite.Driver
    controller_class = controllers.ClaimController
