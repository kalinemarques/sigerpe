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
    else:
        print("As senhas não são iguais.")