from __future__ import print_function
import logging
import os
import sys

from .constants import (
    CONFIG_FILE,
    ERROR,
    WARNING,
    IMAGE_OK,
    IMAGE_WARNING,
    IMAGE_ERROR,
)
from .checks import ALL_CHECKS

PY2 = sys.version_info[0] == 2


def run():
    logging.root.setLevel(logging.ERROR)

    messages = {ERROR: [], WARNING: []}

    config = {}
    config_path = os.path.join(os.getcwd(), CONFIG_FILE)
    try:
        if PY2:
            execfile(config_path, config)
        else:
            exec(open(config_path).read(), config)
    except (FileNotFoundError, IOError):
        messages[ERROR].append('Please create config file {}'.format(config_path))

    run_checks(config, messages)

    if messages[ERROR]:
        print('{} | iconName={}'.format(len(messages[ERROR]), IMAGE_ERROR))
    elif messages[WARNING]:
        print('{} | iconName={}'.format(len(messages[WARNING]), IMAGE_WARNING))
    else:
        print('| iconName={}'.format(IMAGE_OK))

    print('---')

    for msg in messages[ERROR]:
        print('{} | color=#F00'.format(msg))
    for msg in messages[WARNING]:
        print('{} | color=#FA0'.format(msg))

    print('reload | refresh=true')


def run_checks(config, messages):
    checks = config.get('CHECKS', [])

    for check in checks:
        if ALL_CHECKS.get(check):
            ALL_CHECKS[check](config, messages)
