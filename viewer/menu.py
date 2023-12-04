import getpass
from sigerpe.viewer import valida

gerentes = {
    'kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
    'daniel': {'daniel@gmail.com': '12345678'},
    'kaline': {'kaline@gmail.com': 'Qw78@.'}
}

def opcao2():
    email = input('Email: ')
    if valida.check(email):
        valida.verificasenha()
        return True
    else:
        print("Email inválido, por favor digite novamente.")
        email = input('Email: ')

def opcao1():
    usuario = input('Nome de Usuário: ')
    senha = getpass.getpass('Senha: ')
    #VERIFICAR A LISTA DE CLIENTES
    if (senha == 'abc') and (usuario == 'joana'):
        verifica = True
        print('verificou')
    
    if verifica==True:
        print("entrou")
        while True:
            escolha = input("""
                                SiGerPe
        Sistema de Gerenciamento de Pedidos para restaurantes
        

        ___GERENCIAMENTO DE MESAS___                

        [1] - Cadastrar mesa.
        [2] - Aletar mesa. 
        [3] - Listar mesas.  
        [4] - Buscar mesa.                                                            
        [5] - Deletar mesa.
        [6] - Sair.
        """)
            if escolha == '1':
                pass
            if escolha =='2':
                pass
            if escolha == '3':
                pass
            if escolha =='4':
                pass
            if escolha == '5':
                pass
            if escolha =='6':
                break
            else:
                print("Opção inválida!")
        return True
        
escolha = input("""
                            SiGerPe
      Sistema de Gerenciamento de Pedidos para restaurantes
      

                

    [1] - Entrar.    
    [2] - Recuperar senha.
    [3] - Sair.
      """)
verifica = False
while True:
    if escolha == '1':
        if opcao1():
            break

    if escolha == '2':       
        if opcao2():
            break

    if escolha == '3':
        print("Saindo do sistema...")
        break
