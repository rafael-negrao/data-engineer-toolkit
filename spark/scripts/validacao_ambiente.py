from delta import *
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, StringType, StructType, StructField


def get_spark_session():
    builder = (
        pyspark
        .sql
        .SparkSession
        .builder
        .appName("delta")
        .master("spark://spark-master:7077")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.hadoop.fs.s3a.access.key", "datalake")
        .config("spark.hadoop.fs.s3a.secret.key", "datalake")
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    )
    return configure_spark_with_delta_pip(builder).enableHiveSupport().getOrCreate()


def load_data(spark):
    schema = StructType([
        StructField("User_ID", IntegerType(), True),
        StructField("Username", StringType(), True),
        StructField("Browser", StringType(), True),
        StructField("OS", StringType(), True),
    ])
    data = ([
        (1580, "Barry", "FireFox", "Windows"),
        (5820, "Sam", "MS Edge", "Linux"),
        (2340, "Harry", "Vivaldi", "Windows"),
        (7860, "Albert", "Chrome", "Windows"),
        (1123, "May", "Safari", "macOS")
    ])
    return spark.createDataFrame(data, schema=schema)


def transform(spark, dataframe: DataFrame):
    dataframe = dataframe.withColumn('os_', F.lower(F.col('OS')))
    return dataframe


def write(spark, dataframe: DataFrame):
    (
        dataframe
        .write
        .format('delta')
        .mode('overwrite')
        .save('s3a://delta-lake/users_from_airflow')
    )


def pipeline():
    spark = get_spark_session()
    dataframe = load_data(spark)
    dataframe = transform(spark, dataframe)
    write(spark, dataframe)


if __name__ == "__main__":
    pipeline()
