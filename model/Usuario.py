from pymongo import MongoClient
#from projectSus.database import Database
from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, email, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.criado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  

    def salvar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['Usuarios'] 


        usuario_data = {
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "senha": self.senha,
            "criado_em": self.criado_em
        }
        collection.insert_one(usuario_data)
        print(f"Usuário {self.nome} salvo com sucesso!")

