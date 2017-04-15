# Monitoring plugin for Argos

## Available checks

* server load
* Wordpress site up-to-date

## Requirements

* Python 2 or 3
* [Argos](https://github.com/p-e-w/argos) or [BitBar](https://getbitbar.com/)

## Instalation

```bash
sudo pip install argos-plugin-monitoring
ln -s /usr/bin/argos-plugin-monitoring ~/.config/argos/monitoring.5m.py
```

## Configuration

Configuration is stored in file `.config/argos/.monitoring-settings.py`

### Example config

```python
from monitoring import ERROR, WARNING


WORDPRESS_SITES = [
    'example.com',
]

# server: max load
SERVERS = {
    'example.com': 4,
}

CHECKS = [
    'wordpress',
    'server_load',
]

CHECKS_ERROR_LEVELS = {
    'wordpress': WARNING,
    'server_load': ERROR,
}
```
