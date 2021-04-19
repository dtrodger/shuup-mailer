"""
Utils
"""

from __future__ import annotations
import logging
import os
import importlib
import sys


log = logging.getLogger(__name__)


ENV_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", ".env")


def get_module(module_name):
    return sys.modules.get(module_name, importlib.import_module(module_name))


def get_object(module_name, obj):
    module = get_module(module_name)
    return getattr(module, obj)


def has_object(module_name, obj):
    module = get_module(module_name)
    return hasattr(module, obj)


def has_module(module_name):
    return True if importlib.util.find_spec(module_name) else False


def get_instance(module, cls, *args, **kwargs):
    return get_object(module, cls)(*args, **kwargs)


def go(object_path):
    module_name, obj = object_path.rsplit(".", 1)
    return get_object(module_name, obj)


def ho(object_path):
    module_name, obj = object_path.rsplit(".", 1)
    return has_object(module_name, obj)


def gi(cls_path, *args, **kwargs):
    module, cls = cls_path.rsplit(".", 1)
    return get_instance(module, cls, *args, **kwargs)


def set_env_var(key, value, is_list=False, is_bool=False, is_int=False, exce=True):
    """
    Sets environment variables
    """
    if exce:
        if os.environ.get(key):
            raise ValueError(f"Environment {key} variable already exists")

    if is_list:
        value = value.split(",")
    elif is_int:
        value = int(value)
    elif is_bool:
        lower_val = value.lower()
        if lower_val in ["t", "true"]:
            value = True
        elif lower_val in ["f", "false"]:
            value = False

    os.environ[key] = value


def get_env_var(
    key, default=None, is_list=False, is_bool=False, is_int=False, exce=True
):
    """
    Gets environment variables
    """
    if exce:
        value = os.environ[key]
    else:
        value = os.environ.get(key, default)

    if is_list:
        value = value.split(",")
    if is_int:
        value = int(value)
    elif is_bool:
        lower_val = value.lower()
        if lower_val in ["t", "true"]:
            value = True
        elif lower_val in ["f", "false"]:
            value = False

    elif value == "NONE":
        value = None

    return value
