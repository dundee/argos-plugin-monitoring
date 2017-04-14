from __future__ import print_function
import logging
import os
import sys

from .wordpress import check_wordpress_domains

PY2 = sys.version_info[0] == 2

CONFIG_FILE = '.config/argos/.monitoring-settings.py'

ERROR = 0
WARNING = 1


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
        print('{} | iconName=error-symbolic'.format(len(messages[ERROR])))
    elif messages[WARNING]:
        print('{} | iconName=important'.format(len(messages[WARNING])))
    else:
        print('OK | color=#0F0')

    print('---')

    for msg in messages[ERROR]:
        print('{} | color=#F00'.format(msg))
    for msg in messages[WARNING]:
        print('{} | color=#FA0'.format(msg))

    print('reload | refresh=true')


def run_checks(config, messages):
    checks = config.get('CHECKS', [])

    for check in checks:
        if check == 'wordpress':
            check_wordpress_domains(config, messages)
