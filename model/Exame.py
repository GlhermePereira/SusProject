from pymongo import MongoClient
from datetime import datetime

class Exame:
    def __init__(self, paciente_id, tipo, resultado, medico_id, data_realizacao):
        self.paciente_id = paciente_id
        self.tipo = tipo
        self.resultado = resultado
        self.medico_id = medico_id
        self.data_realizacao = data_realizacao
        self.criado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  # Formata a data no formato desejado

    def salvar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['Exames']
        exame_data = {
            "paciente_id": self.paciente_id,
            "tipo": self.tipo,
            "resultado": self.resultado,
            "medico_id": self.medico_id,
            "data_realizacao": self.data_realizacao,
            "criado_em": self.criado_em
        }
        collection.insert_one(exame_data)
        print("Exame cadastrado com sucesso!")
