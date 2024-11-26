from pymongo import MongoClient
from datetime import datetime
class Agendamento:
    def __init__(self, paciente_id, data_horario, especialidade):
        self.paciente_id = paciente_id
        self.data_horario = data_horario
        self.especialidade = especialidade
        self.criado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  # Formata a data no formato desejado

    def agendar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['Consultas']  # Usando a coleção correta para consultas.
        consulta_data = {
            "paciente_id": self.paciente_id,
            "data_horario": self.data_horario,
            "especialidade": self.especialidade,
            "status": "pendente",
            "criado_em": self.criado_em
        }
        collection.insert_one(consulta_data)
        print(f"Consulta para o paciente {self.paciente_id} agendada com sucesso!")
