# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This modules contains read-only constants used throughout
the presto admin project.
"""

import os

import prestoadmin

# Logging Config File Locations
LOGGING_CONFIG_FILE_NAME = 'presto-admin-logging.ini'
LOGGING_CONFIG_FILE_DIRECTORIES = [
    os.path.join(prestoadmin.main_dir, 'prestoadmin')
]

# local configuration
LOG_DIR_ENV_VARIABLE = 'PRESTO_ADMIN_LOG_DIR'
CONFIG_DIR_ENV_VARIABLE = 'PRESTO_ADMIN_CONFIG_DIR'
LOCAL_CONF_DIR = '.prestoadmin'
DEFAULT_LOCAL_CONF_DIR = os.path.join(os.path.expanduser('~'), LOCAL_CONF_DIR)
TOPOLOGY_CONFIG_FILE = 'config.json'
COORDINATOR_DIR_NAME = 'coordinator'
WORKERS_DIR_NAME = 'workers'
CATALOG_DIR_NAME = 'catalog'
PRESTO_REMOTE_CONF_DIR = 'PRESTO_REMOTE_CONF_DIR'
PRESTO_REMOTE_PACKAGES_PATH = 'PRESTO_REMOTE_PACKAGES_PATH'
PRESTO_REMOTE_SERVER_LOG_FILE = 'PRESTO_REMOTE_SERVER_LOG_FILE'
PRESTO_REMOTE_LAUNCHER_LOG_FILE = 'PRESTO_REMOTE_LAUNCHER_LOG_FILE'
PRESTO_REMOTE_PLUGIN_DIR = 'PRESTO_REMOTE_PLUGIN_DIR'

# remote configuration
REMOTE_CONF_DIR = os.environ[PRESTO_REMOTE_CONF_DIR] \
                  if PRESTO_REMOTE_CONF_DIR in os.environ else '/etc/presto'
REMOTE_CATALOG_DIR = os.path.join(REMOTE_CONF_DIR, 'catalog')
REMOTE_PACKAGES_PATH = os.environ[PRESTO_REMOTE_PACKAGES_PATH] \
                       if PRESTO_REMOTE_PACKAGES_PATH in os.environ \
                       else '/opt/prestoadmin/packages'
DEFAULT_PRESTO_SERVER_LOG_FILE = os.environ[PRESTO_REMOTE_SERVER_LOG_FILE] \
                                 if PRESTO_REMOTE_SERVER_LOG_FILE in os.environ \
                                 else '/var/log/presto/server.log'
DEFAULT_PRESTO_LAUNCHER_LOG_FILE = os.environ[PRESTO_REMOTE_LAUNCHER_LOG_FILE] \
                                   if PRESTO_REMOTE_LAUNCHER_LOG_FILE in os.environ \
                                   else '/var/log/presto/launcher.log'
REMOTE_PLUGIN_DIR = os.environ[PRESTO_REMOTE_PLUGIN_DIR] \
                    if PRESTO_REMOTE_PLUGIN_DIR in os.environ \
                    else '/usr/lib/presto/lib/plugin'
REMOTE_COPY_DIR = '/tmp'

# Presto configuration files
CONFIG_PROPERTIES = "config.properties"
LOG_PROPERTIES = "log.properties"
JVM_CONFIG = "jvm.config"
NODE_PROPERTIES = "node.properties"
