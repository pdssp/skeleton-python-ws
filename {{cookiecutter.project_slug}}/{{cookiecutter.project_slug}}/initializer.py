# {{cookiecutter.project_name}} - {{cookiecutter.project_short_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
#
# This file is part of {{cookiecutter.project_name}}.
#
# {{cookiecutter.project_name}} is free software: you can redistribute it and/or modify
# it under the terms of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} for more details.
#
# You should have received a copy of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %}
# along with {{cookiecutter.project_name}}.  If not, see <https://www.gnu.org/licenses/>.
"""Initialization of the server"""
from fastapi import FastAPI
from tortoise.contrib.starlette import register_tortoise

from .config import tortoise_config
from .core.routers import router_web_site, router_ws


def init(app: FastAPI):
    """
    Init routers and etc.
    :return:
    """
    init_routers(app)
    init_db(app)


def init_db(app: FastAPI):
    """
    Init database models.
    :param app:
    :return:
    """
    register_tortoise(
        app,
        db_url=tortoise_config.db_url,
        generate_schemas=tortoise_config.generate_schemas,
        modules=tortoise_config.modules,
    )


def init_routers(app: FastAPI):
    """
    Initialize routers defined in `app.api`
    :param app:
    :return:
    """
    app.include_router(
        router_ws,
        prefix="/ws",
        responses={404: {"description": "Not found"}},
    )
    app.include_router(
        router_web_site,
        tags=["Web site"],
        responses={404: {"description": "Not found"}},
    )
