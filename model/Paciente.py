from pymongo import MongoClient
from datetime import datetime

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, endereco, telefone, usuario_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco  # Dicionário com informações do endereço
        self.telefone = telefone
        self.usuario_id = usuario_id
        self.criado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  # Formata a data no formato desejado

    def salvar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['Pacientes']  # Coleção para armazenar os pacientes
        paciente_data = {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "usuario_id": self.usuario_id,
            "criado_em": self.criado_em
        }
        collection.insert_one(paciente_data)
        print(f"Paciente {self.nome} cadastrado com sucesso!")