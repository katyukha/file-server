#!/usr/bin/env python
import bottle
from bottle.ext import sqlalchemy
from models import Base

from settings import SQLALCHEMY_ENGINE

from sqlalchemy import create_engine

engine = create_engine(SQLALCHEMY_ENGINE, echo=True)

uploader = bottle.Bottle()
plugin = sqlalchemy.Plugin(
    engine, # SQLAlchemy engine created with create_engine function.
    Base.metadata, # SQLAlchemy metadata, required only if create=True.
    keyword='db', # Keyword used to inject session database in a route (default 'db').
    create=True, # If it is true, execute `metadata.create_all(engine)` when plugin is applied (default False).
    commit=True, # If it is true, plugin commit changes after route is executed (default True).
    use_kwargs=True# If it is true and keyword is not defined, plugin uses **kwargs argument to inject session database (default False).
)

uploader.install(plugin)
