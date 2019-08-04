#!/usr/bin/env python
# This file is part of the technical-challlenge-be project
# https://github.com/technical_challenge_be/technical-challlenge-be
#
# Copyright (c) 2019 Atef Arfaoui (arfatef@gmail.com) - All Rights Reserved
# SPDX-License-Identifier: Proprietary
import os
import click
import technical_challlenge_be


# To enable pretty tracebacks:
#   echo "export ENABLE_BACKTRACE=1;" >> ~/.bashrc
if os.environ.get('ENABLE_BACKTRACE') == "1":
    try:
        import backtrace
        backtrace.hook(align=True, strip_path=True, enable_on_envvar_only=True)
    except ImportError:
        # don't fail just because of missing dev library
        pass


click.disable_unicode_literals_warning = True


@click.group()
def cli() -> None:
    """technical_challlenge_be cli."""


@cli.command()
@click.version_option(version="v201908.0001-alpha")
def version() -> None:
    """Show version number."""
    print(f"technical_challlenge_be version: {technical_challlenge_be.__version__}")
