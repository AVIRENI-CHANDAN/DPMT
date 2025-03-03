import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError as e:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable") from e
