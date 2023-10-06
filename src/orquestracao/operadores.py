from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class MeuNovoCustomOperator(BaseOperator):
    """
    MeuNovoCustomOperator.
    """

    @apply_defaults
    def __init__(self, atributo_1, **kwargs):
        """
        Constructor for MeuNovoCustomOperator.

        :param atributo_1: Um parâmetro específico para o seu operador.
        :type atributo_1: str
        """
        BaseOperator.__init__(self, **kwargs) # deixando mais flexivel se tiver heranca multipla
        self.atributo_2 = atributo_1

    def execute(self, context):
        """
        Lógica principal do operador. Será chamado quando a tarefa for executada.

        :param context: O contexto do Airflow, que contém informações sobre a execução da tarefa.
        :type context: dict
        """
        self.log.info(f"Executando MeuNovoCustomOperator com my_parameter: {self.atributo_2}")
        # Coloque sua lógica de tarefa aqui
        # Você pode acessar informações do contexto, como dag_run, execution_date, etc.
