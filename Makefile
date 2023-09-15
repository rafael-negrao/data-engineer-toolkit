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


export-requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt


env-local-dev-stop:
	docker-compose -f docker-compose.yml stop &


env-local-dev-down: env-local-dev-stop
	docker-compose -f docker-compose.yml down &


env-local-dev-start: env-local-dev-down export-requirements
	docker-compose -f docker-compose.yml up --build &

