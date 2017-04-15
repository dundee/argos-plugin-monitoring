
from .server_load import check_load_of_servers
from .wordpress import check_wordpress_domains

ALL_CHECKS = {
    'wordpress': check_wordpress_domains,
    'server_load': check_load_of_servers,
}
