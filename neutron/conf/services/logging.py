# Copyright 2017 Fujitsu Limited
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from oslo_config import cfg

from neutron._i18n import _

log_driver_opts = [
    cfg.IntOpt(
        'rate_limit',
        default=100,
        min=100,
        help=_('Maximum packets logging per second.')),
    cfg.IntOpt(
        'burst_limit',
        default=25,
        min=25,
        help=_('Maximum number of packets per rate_limit.')),
    cfg.StrOpt(
        'local_output_log_base',
        help=_('Output logfile path on agent side, default syslog file.')),
]


def register_log_driver_opts(cfg=cfg.CONF):
    cfg.register_opts(log_driver_opts, 'network_log')
