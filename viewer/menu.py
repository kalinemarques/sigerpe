import os
import getpass
from viewer import valida
from controller.mesaController import CadastrarMesa, ExcluirMesa, BuscarMesa, ListarMesa, AlterarMesa
 
def opcao1():
    usuario = input('Nome de Usuário: ').lower()
    senha = getpass.getpass('Senha: ')
    teste = valida.validaEntrada(usuario, senha) 
    if teste == True:
        while True:
            escolha = input("""
         _______________________________________________________                    
        |                                                       | 
        |                         SiGerPe                       |
        | Sistema de Gerenciamento de Pedidos para restaurantes |
        |_______________________________________________________|
        |                                                       |
        |              ___GERENCIAMENTO DE MESAS___             |   
        |                                                       |
        |  [1] - Cadastrar mesa.                                |
        |  [2] - Alterar mesa.                                  |
        |  [3] - Listar mesas.                                  |
        |  [4] - Buscar mesa.                                   |                                      
        |  [5] - Deletar mesa.                                  |
        |  [6] - Voltar.                                        |
        |  [7] - Sair.                                          |
        |_______________________________________________________|
        """)
            os.system('cls')
            try:
                if escolha == '1':
                    print('___CADASTRO DE MESAS___\n')
                    qtdMesa = int(input("Insira capacidade de pessoas na mesa: "))
                    idGarcom = int(input("Insira o id do garçom: "))
                    CadastrarMesa.post(qtdMesa, idGarcom)
                    print("Mesa cadastrada com sucesso!")
                if escolha == '2':
                    print('___ALTERAR MESA___\n')
                    idGarcom = int(input("Insira o id do novo garçom: "))
                    idMesa = int(input("Insira o id da mesa: "))                
                    AlterarMesa.get(idMesa, idGarcom) 
                    print("Update realizado com sucesso!")              
                if escolha == '3':
                    print("___Lista de mesas___\n")
                    ListarMesa.get()
                if escolha == '4':
                    print("___Busca___\n")
                    idMesa = int(input("Insira o id da mesa: "))
                    BuscarMesa.get(idMesa)
                    

                if escolha == '5':
                    print("___Deletar___\n")
                    idMesa = int(input("Insira o ID da mesa: "))
                    ExcluirMesa.get(idMesa)
                    print("Mesa deletada com sucesso!")
                if escolha == '6':
                    return False
                if escolha == '7':
                    break
                if escolha not in {'1', '2', '3', '4', '5', '6', '7'}:
                    print("Opção inválida!")
            except IndexError:
                print("Mesa não encontrada no banco de dados.")
            except ValueError:
                print("Por favor, insira um ID de mesa válido (número inteiro).")
        return True

escolha = input("""
         _______________________________________________________                    
        |                                                       | 
        |                        SiGerPe                        |
        | Sistema de Gerenciamento de Pedidos para restaurantes |
        |_______________________________________________________|
        |                                                       |                
        |                     ___LOGIN___                       |
        |                                                       |                
        | [1] - Entrar.                                         |
        | [2] - Sair                                            |
        |                                                       |
        |_______________________________________________________|        
      """)
verifica = False
os.system('cls')

while True:
    while escolha not in {'1', '2'}:
        print("Opção inválida.")
        escolha = input("Digite novamente: ")

    if escolha == '1':
        if opcao1():
            break

    """ if escolha == '2':       
        if not opcao2():
            break"""

    if escolha == '2':
        print("Saindo do sistema...")
        break
