import subprocess


def check_load_of_servers(config, messages):
    if 'server_load' not in config.get('CHECKS_ERROR_LEVELS', {}):
        messages[0].append('Please set CHECKS_ERROR_LEVELS variable')
        return
    error_level = config['CHECKS_ERROR_LEVELS']['server_load']

    for server, max_load in config.get('SERVERS', {}).items():
        res = subprocess.check_output(['ssh', server, 'cat', '/proc/loadavg'])
        load_avg_5m = float(res.split()[1])
        if load_avg_5m > max_load:
            messages[error_level].append(
                'Load of server {} is {}'.format(
                    server,
                    load_avg_5m,
                )
            )
