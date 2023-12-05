import re
import getpass

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def check(email):  
  
    if(re.search(regex,email)):
        #verificar se está no dicionário  
        return True           
    else:  
       return False

def verificasenha():
    senha = getpass.getpass("Nova senha: ")
    senha2 = getpass.getpass("Por favor confirme a senha.\nSenha: ")
    if senha == senha2:
        print("Senha alterada com sucesso!")
        return True
    else:
        print("As senhas não são iguais.")
        return False

def validaEntrada(nome, senha):
    gerentes = {
        'kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
        'daniel': {'daniel@gmail.com': '12345678'},
        'kaline': {'kaline@gmail.com': 'Qw78@.'},
        'joamerson': {'joamerson@gmail.com': 'senha'}
    }

    if nome in gerentes and senha == gerentes[nome].get(list(gerentes[nome].keys())[0]):
        return True
    else:
        print("Os dados fornecidos estão incorretos.")
        return False
    
def emailCadastrado(email):
    gerentes = {
        'kaliane': {'kaliane@gmail.com': 'amoGoiaba'},
        'daniel': {'daniel@gmail.com': '12345678'},
        'kaline': {'kaline@gmail.com': 'Qw78@.'},
        'joamerson': {'joamerson@gmail.com': 'senha'}
    }

    for dadosGerentes in gerentes.values():
        if email in dadosGerentes:
            return True

    print("O e-mail fornecido não está cadastrado.")
    return False

'''# Example usage:
nome_usuario = input("Nome de Usuário: ")
senha_usuario = input("Senha: ")

if validaEntrada(nome_usuario, senha_usuario):
    print("Acesso concedido.")
else:
    print("Acesso negado.")'''
