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


install: test
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


env-local-dev-stop:
	docker-compose -f docker-compose.yml stop &


env-local-dev-down: env-local-dev-stop
	docker-compose -f docker-compose.yml down &


env-local-dev-start: env-local-dev-down export-requirements
	docker-compose -f docker-compose.yml up --build &


env-local-start-all-spark-notebook: env-local-dev-down
	docker-compose up minio spark-master spark-worker-1 spark-worker-2 all-spark-notebook &


env-local-start-all-spark-notebook-airflow: env-local-dev-down
	docker-compose up minio spark-master spark-worker-1 spark-worker-2 all-spark-notebook postgres redis airflow-init airflow-webserver airflow-scheduler airflow-worker airflow-triggerer airflow-cli flower &

