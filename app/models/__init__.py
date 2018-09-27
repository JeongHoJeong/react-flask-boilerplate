import os.path
import glob
import importlib

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()


class OrmBase(Base):  # type: ignore
    __abstract__ = True
    metadata = metadata


modules = glob.glob(os.path.dirname(__file__) + '/*.py')
for f in modules:
    if not (f.endswith('__init__.py') and f.startswith('_')):
        module_name = os.path.basename(f)[:-3]
        importlib.import_module('app.models.{}'.format(module_name))
