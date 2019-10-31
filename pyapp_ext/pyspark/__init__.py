"""
pyApp - PySpark
"""
from .__version__ import __version__
from .factory import *

version_info = tuple(int(v) for v in __version__.split("."))


class Extension:
    """
    pyApp PySpark
    """

    default_settings = ".default_settings"

    @staticmethod
    def ready():
        from pyapp.injection import register_factory

        register_factory(SparkSession, session_factory)
