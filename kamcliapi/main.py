# Copyright 2019 The Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from configparser import ConfigParser, Error as ConfigParserError
from typing import Optional

import click
import uvicorn  # type: ignore

from .app import get_app


@click.command()
@click.option(
    "-c", "--config-file", type=click.Path(), help="Path to the configuration file"
)
@click.option(
    "--host",
    type=str,
    default="127.0.0.1",
    help="Bind socket to this host",
    show_default=True,
)
@click.option(
    "--port", type=int, default=8000, help="Bind socket to this port", show_default=True
)
@click.option(
    "--debug", is_flag=True, default=False, help="Enable debug mode", hidden=True
)
def main(
    config_file: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    debug: bool = False,
):
    config = dict(
        host=host,
        port=port,
        debug=debug,
    )
    if config_file is not None:
        parser = ConfigParser()
        try:
            parser.read(config_file)
        except ConfigParserError:
            raise click.UsageError("Invalid configuration file")
        for k, v in parser['DEFAULT'].items():
            config[k] = v
    app = get_app(config)
    log_level = "info" if not config['debug'] else "debug"
    uvicorn.run(
        app,
        host=config['host'],
        port=config['port'],
        log_level=log_level,
        reload=config['debug'],
    )


def main_with_env():
    main(auto_envvar_prefix="KAMCLI_API")

