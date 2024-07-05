# data engineer toolkit

Este projeto tem como objetivo fornecer um conjunto de ferramentas para permitir o estudo da engenharia de dados

## Requisitos

Ter instalado:

- docker
- docker-compose
- make
- python
- poetry

## make

Foi utilizado o make para:

- Organizar a compilação do projeto python
- Construição das imagens base para o Apache Airflow, Apache Spark e Jupyter
- Inicialização do docker compose

## Projeto Python

Principais comandos:

- **make clean**
    - Remove os diretórios `dist` e `target`
        - `dist`: fontes empacotados no formato `whl` e `tar.gz`
        - `target`: fontes do projeto com as respectivas dependências
- **make build**
    - Faz a atualização do poetry e compilação do projeto
- **make package**
    - Faz o empacotamento do projeto nos diretórios `dist` e `target`
        - `dist`: fontes empacotados no formato `whl` e `tar.gz`
        - `target`: fontes do projeto com as respectivas dependências
- **make test**
    - Executa os testes planejados nos diretório `test`
- **make install**
    - Faz a instalação do projeto como library no env local da máquina
- **make export-requirements**
    - Gera o arquivo requirements.txt

## Docker

Principais comandos:

- **make docker-build-image-airflow**
    - Monta a imagem do airflow usando como referência o arquivo [airflow.Dockerfile](airflow.Dockerfile)
- **make docker-build-image-spark**
    - Monta a imagem do spark
    - O projeto de referência está no diretório [spark/build-image](spark%2Fbuild-image)
- **docker-build-image-spark-win**
    - Monta a imagem do spark
    - O projeto de referência está no diretório [spark/build-image](spark%2Fbuild-image)
- **make docker-build-image-jupyter**
    - Monta a imagem do jupyter usando como referência o arquivo [jupyter.Dockerfile](jupyter.Dockerfile)

## Docker Run - Apache Airflow e Apache Spark

Principais comando:

- **make env-local-dev-stop_all-spark-notebook-airflow**
    - Para a execução do ambiente docker
- **make env-local-dev-down_all-spark-notebook-airflow**
    - Para a execução do ambiente docker e remove os containers
- **make env-local-dev-start_all-spark-notebook-airflow**
    - Inicializa todos os serviços contidos no arquivo [docker-compose_all-spark-notebook-airflow.yml](docker-compose_all-spark-notebook-airflow.yml)

## Docker Run - Apache Spark

Principais comando:

- **make env-local-dev-stop_all-spark-notebook**
    - Para a execução do ambiente docker
- **make env-local-dev-down_all-spark-notebook**
    - Para a execução do ambiente docker e remove os containers
- **make env-local-dev-start_all-spark-notebook**
    - Inicializa todos os serviços contidos no arquivo [docker-compose_all-spark-notebook.yml](docker-compose_all-spark-notebook.yml)

## Docker Run - Apache Kafka

Principais comando:

- **make env-local-dev-stop_kafka**
    - Para a execução do ambiente docker
- **make env-local-dev-down_kafka**
    - Para a execução do ambiente docker e remove os containers
- **make env-local-dev-start_kafka**
    - Inicializa todos os serviços contidos no arquivo [docker-compose_kafka.yml](docker-compose_kafka.yml)

## Serviços Docker

| Nome do Serviço    | Descrição                                       | Portas                                                                                          |
|--------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------|
| postgres           | Serviço de Banco de dados                       |                                                                                                 |
| redis              | Serviço de Banco de dados NoSQL em memória      | [6379](http://localhost:6379)                                                                   |
| airflow-webserver  | Apache Airflow - Componente Web UI              | [8080](http://localhost:8080)                                                                   |
| airflow-scheduler  | Apache Airflow - Componente Scheduler           |                                                                                                 |
| airflow-worker     | Apache Airflow - Componente Worker (celery)     |                                                                                                 |
| airflow-triggerer  | Apache Airflow - Componente Triggerer           |                                                                                                 |
| airflow-init       | Apache Airflow - Init, faz o setup do ambiente  |                                                                                                 |
| airflow-cli        | Apache Airflow - Componente Cli                 |                                                                                                 |
| flower             | Apache Airflow - Componente Flower              | [5555](http://localhost:5555)                                                                   |
| minio              | Min IO, simula o serviço do s3 (object storage) |                                                                                                 |
| spark-master       | Apache Spark - Master                           | [18080](http://localhost:18080), [14040](http://localhost:14040), [7077](http://localhost:7077) |
| spark-worker-1     | Apache Spark - Worker                           | [18081](http://localhost:18081), [27077](http://localhost:27077)                                |
| spark-worker-1     | Apache Spark - Worker                           | [28081](http://localhost:28081), [37077](http://localhost:37077)                                |
| all-spark-notebook | Jupyter                                         | [4041](http://localhost:4041), [7080](http://localhost:7080), [8888](http://localhost:8888)     |
| zookeeper          | Zookeeper                                       | [2181](http://localhost:2181)                                                                   |
| broker             | Kafka Broker                                    | [9092](http://localhost:9092), [9101](http://localhost:9101)                                    |
| schema-registry    | Schema Registry                                 | [8081](http://localhost:8081)                                                                   |
| connect            | Kafka Connect                                   | [8083](http://localhost:8083)                                                                   |
| control-center     |                                                 |                                                                                                 |
| ksqldb-server      |                                                 |                                                                                                 |
| ksqldb-cli         |                                                 |                                                                                                 |
| rest-proxy         |                                                 |                                                                                                 |
