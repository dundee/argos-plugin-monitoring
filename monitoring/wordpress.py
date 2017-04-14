from wp_version_checker import check_domains, get_version_installed_on_domain, get_current_version


def check_wordpress_domains(config, messages):
    if not config.get('WORDPRESS_ERROR_LEVEL'):
        messages[0].append('Please set WORDPRESS_ERROR_LEVEL variable')
        return

    if config.get('WORDPRESS_SITES'):
        failed = check_domains(config['WORDPRESS_SITES'])

        if failed:
            curr_version = get_current_version()

        for domain in failed:
            messages[config['WORDPRESS_ERROR_LEVEL']].append(
                'Wordpress on domain {} is outdated. Current version is {}, but running {}'.format(
                    domain,
                    curr_version,
                    get_version_installed_on_domain(domain),
                )
            )
