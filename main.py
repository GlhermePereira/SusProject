from model.Usuario import Usuario
from model.Agendamento import Agendamento
from model.Paciente import Paciente
from model.Exame import Exame
from model.Notificacao import Notificacao
from model.FilaAtendimento import FilaAtendimento

def main():
    while True:
        print("\n=== Sistema SUS ===")
        print("1. Cadastrar Usuário")
        print("2. Agendar Consulta")
        print("3. Cadastrar Paciente")
        print("4. Cadastrar Exame")
        print("5. Enviar Notificação")
        print("6. Cadastrar na Fila de Atendimento")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Cadastrar Usuário
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            senha = input("Senha: ")
            usuario = Usuario(nome, cpf, email, telefone, senha)
            usuario.salvar()
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":  # Agendar Consulta
            paciente_id = input("ID do Paciente: ")
            data_horario = input("Data e Hora (YYYY-MM-DD HH:MM): ")
            especialidade = input("Especialidade: ")
            consulta = Agendamento(paciente_id, data_horario, especialidade)
            consulta.agendar()
            print(f"Consulta agendada: {consulta}")

        elif opcao == "3":  # Cadastrar Paciente
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
            cpf = input("CPF: ")
            endereco = {
                "rua": input("Rua: "),
                "numero": input("Número: "),
                "cidade": input("Cidade: "),
                "estado": input("Estado: "),
                "cep": input("CEP: ")
            }
            telefone = input("Telefone: ")
            usuario_id = input("ID do Usuário: ")
            paciente = Paciente(nome, data_nascimento, cpf, endereco, telefone, usuario_id)
            paciente.salvar()
            print(f"Paciente {nome} cadastrado com sucesso!")

        elif opcao == "4":  # Cadastrar Exame
            paciente_id = input("ID do Paciente: ")
            tipo = input("Tipo do Exame: ")
            resultado = {
                "arquivo_url": input("URL do Arquivo do Resultado: "),
                "descricao": input("Descrição do Resultado: ")
            }
            medico_id = input("ID do Médico: ")
            data_realizacao = input("Data de Realização (YYYY-MM-DD HH:MM): ")
            exame = Exame(paciente_id, tipo, resultado, medico_id, data_realizacao)
            exame.salvar()
            print("Exame cadastrado com sucesso!")

        elif opcao == "5":  # Enviar Notificação
            usuario_id = input("ID do Usuário: ")
            tipo = input("Tipo de Notificação: ")
            mensagem = input("Mensagem: ")
            status = input("Status (Enviado/Pendente): ")
            notificacao = Notificacao(usuario_id, tipo, mensagem, status)
            notificacao.salvar()
            print("Notificação enviada com sucesso!")

        elif opcao == "6":  # Cadastrar na Fila de Atendimento
            consulta_id = input("ID da Consulta: ")
            paciente_id = input("ID do Paciente: ")
            status_atendimento = input("Status do Atendimento (Aguardando/Em Atendimento/Finalizado): ")
            fila = FilaAtendimento(consulta_id, paciente_id, status_atendimento)
            fila.salvar()
            print("Entrada na fila de atendimento cadastrada com sucesso!")

        elif opcao == "7":  # Sair
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
