#FROM apache/airflow:2.7.1
FROM apache/airflow:2.7.1-python3.8
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-11-jre-headless \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
RUN pip install --no-cache-dir --force-reinstall delta-spark==2.1.0 pyspark==3.3.0
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" apache-airflow-providers-apache-spark==4.1.5