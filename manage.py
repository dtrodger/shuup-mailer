#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line
import dotenv


if __name__ == "__main__":
    dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shuup.settings")

    execute_from_command_line(sys.argv)
