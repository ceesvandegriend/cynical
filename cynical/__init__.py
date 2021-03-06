import logging
import os
import pathlib

import yaml

import cynical.common.logger


def __setup():
    config = {}
    home_dir = pathlib.Path.home()
    etc_dir = os.path.join(home_dir, 'etc')
    yml = os.path.join(etc_dir, 'cynical.yml')

    if os.path.isfile(yml):
        with open(yml, 'r') as stream:
            config = yaml.safe_load(stream)

    # default: loglevel
    if not 'loglevel' in config:
        config['loglevel'] = logging.INFO

    # default: ~/Maildir
    if not 'maildir' in config:
        config['maildir'] = os.path.join(home_dir, 'Maildir')

    # default: /var/opt/cynical/cynical-email.db
    if not 'db' in config:
        config['db'] = os.path.join('/var', 'opt', 'cynical', 'cynical-email.db')

    return config


__author__ = 'Cees van de Griend <cees@griend.eu>'

config = __setup()

cynical.common.logger.setup(config['loglevel'])
