FROM jupyter/all-spark-notebook:python-3.8.13

USER ${NB_UID}

RUN pip install --no-cache-dir --force-reinstall delta-spark==2.1.0 pyspark==3.3.0
