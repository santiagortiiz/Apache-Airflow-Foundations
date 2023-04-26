from airflow.models.baseoperator import BaseOperator

class MyOperator(BaseOperator):

    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        print(f"Hello {self.name}")