from pymongo import MongoClient
from datetime import datetime

class Notificacao:
    def __init__(self, usuario_id, tipo, mensagem, status):
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.mensagem = mensagem
        self.enviado_em = datetime.now().strftime('%d-%m-%Y %H:%M')  # 
        self.status = status

    def salvar(self):
        client = MongoClient("mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority")
        db = client['SusBd']
        collection = db['Notificacoes']
        notificacao_data = {
            "usuario_id": self.usuario_id,
            "tipo": self.tipo,
            "mensagem": self.mensagem,
            "enviado_em": self.enviado_em,
            "status": self.status
        }
        collection.insert_one(notificacao_data)
        print("Notificação cadastrada com sucesso!")
