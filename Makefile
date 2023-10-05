RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)


clean:
	@rm -rf dist target


build: clean
	@poetry update
	@poetry build


package: build
	@poetry run pip install --upgrade -t target dist/*.whl


test: package
	@poetry run python run_tests.py


install: tests
	@poetry install


docker-build-image-airflow:
	@docker build . -f airflow.Dockerfile --pull --tag apache/airflow:2.7.1


docker-build-image-spark:
	@bash ./spark/build-image/build_from_make.sh


docker-build-image-jupyter:
	@docker build . -f jupyter.Dockerfile --pull --tag jupyter/all-spark-notebook:python-3.8.13


docker-build-images: docker-build-image-airflow docker-build-image-spark docker-build-image-jupyter


export-requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt


env-local-dev-stop_all-spark-notebook-airflow:
	docker-compose -f docker-compose_all-spark-notebook-airflow.yml stop


env-local-dev-down_all-spark-notebook-airflow: env-local-dev-stop_all-spark-notebook-airflow
	docker-compose -f docker-compose_all-spark-notebook-airflow.yml down


env-local-dev-start_all-spark-notebook-airflow: env-local-dev-down_all-spark-notebook-airflow
	docker-compose -f docker-compose_all-spark-notebook-airflow.yml up


env-local-dev-stop_all-spark-notebook:
	docker-compose -f docker-compose_all-spark-notebook.yml stop


env-local-dev-down_all-spark-notebook: env-local-dev-stop_all-spark-notebook
	docker-compose -f docker-compose_all-spark-notebook.yml down


env-local-dev-start_all-spark-notebook: env-local-dev-down_all-spark-notebook
	docker-compose -f docker-compose_all-spark-notebook.yml up


env-local-dev-stop_kafka:
	docker-compose -f docker-compose_kafka.yml stop


env-local-dev-down_kafka: env-local-dev-stop_kafka
	docker-compose -f docker-compose_kafka.yml down


env-local-dev-start_kafka: env-local-dev-down_kafka
	docker-compose -f docker-compose_kafka.yml up