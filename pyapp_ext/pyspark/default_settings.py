SPARK_SESSION = {"default": {}}
"""
PySpark session definition

Local Session::

    SPARK_SESSION = {
        "default": {
            "master": "local",
            "appName": "Word Count",
            "config": {
                "spark.some.config.option": "some-value",
            }
        }
    }

Cluster::

    SPARK_SESSION = {
        "default": {
            "master": "spark://master:7077",
            "appName": "Word Count",
            "config": {
                "spark.some.config.option": "some-value",
            }
        }
    }

"""
