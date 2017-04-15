from wp_version_checker import check_domains, get_version_installed_on_domain, get_current_version


def check_wordpress_domains(config, messages):
    if 'wordpress' not in config.get('CHECKS_ERROR_LEVELS', {}):
        messages[0].append('Please set CHECKS_ERROR_LEVELS variable')
        return
    error_level = config['CHECKS_ERROR_LEVELS']['wordpress']

    if config.get('WORDPRESS_SITES'):
        failed = check_domains(config['WORDPRESS_SITES'])

        if failed:
            curr_version = get_current_version()

        for domain in failed:
            messages[error_level].append(
                'Wordpress on domain {} is outdated. Current version is {}, but running {}'.format(
                    domain,
                    curr_version,
                    get_version_installed_on_domain(domain),
                )
            )
