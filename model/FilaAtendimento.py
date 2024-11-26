from pymongo import MongoClient
from datetime import datetime

class FilaAtendimento:
    def __init__(self, consulta_id, paciente_id, status_atendimento):
        self.consulta_id = consulta_id
        self.paciente_id = paciente_id
        self.status_atendimento = status_atendimento
        self.atualizado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  

    def salvar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['FilaAtendimento']
        fila_data = {
            "consulta_id": self.consulta_id,
            "paciente_id": self.paciente_id,
            "status_atendimento": self.status_atendimento,
            "atualizado_em": self.atualizado_em
        }
        collection.insert_one(fila_data)
        print("Entrada na fila de atendimento cadastrada com sucesso!")
