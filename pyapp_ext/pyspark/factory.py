from pyspark.sql import SparkSession
from pyapp.conf.helpers import NamedFactory

__all__ = ("SparkSession", "session_factory", "get_spark_session")


class SparkSessionFactory(NamedFactory[SparkSession]):
    """
    Factory for creating My Objects.
    """

    defaults = {
        "master": "local",
        "appName": None,
        "config": {},
    }

    def create(self, name: str = None) -> SparkSession:
        config = self.get(name)

        builder = SparkSession.builder.master(config.get("master"))

        # Optional appName
        name = config.get("appName")
        if name:
            builder.appName(name)

        # Apply config args
        for key, value in config.get("config").items():
            builder.config(key, value)

        return builder.getOrCreate()


session_factory = SparkSessionFactory("SPARK_SESSION")
get_spark_session = session_factory.create
