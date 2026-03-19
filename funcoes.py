
dados_all = []

def menu():
 print('\n------ CADASTRO DE PRODUTOS ------ \n ')
 print('1 - Cadastrar\n')
 print('2 - Listar\n')
 print('3 - Excluir\n')
 print('4 - MENU\n')
 print('5 - EDITAR\n')
 print('0 - SAIR\n')

def cadastro():
   codigo =input("Insira o código do produto: ").strip()
   if not(codigo.isnumeric()):
    print('Informe um número válido!')
    menu()
   else:
    nome = input("Insira o produto: ").strip()
    dados_produtos = {
    'cod': codigo,
    'produto': nome.upper()
    }
    dados_all.append(dados_produtos)
    #print(dados_all)
    print('Cadastro realizado com sucesso!')
   return menu()
#
def listar():
 if (len(dados_all)> 0):
    for item in dados_all:
      print(item)
    return True    
 else:
    print('Não existem produtos cadastrados')
    return False
#
def excluir():
  if listar():
   op = input('Qual produto deseja excluir?\n')
   for i, dado in enumerate(dados_all):
    if ((op == dado['cod']) or (op.upper() == dado['produto'])):
       dados_all.remove(dado)
       print('produto excluído com sucesso!')
    menu()
  else:
    return False
#
def editar():
 if listar(): 
  op = input('Qual produto deseja editar?\n')
  for i, dado in enumerate(dados_all):
    if(op == dado['cod']):
       n_cod = input('1 - Novo código do produto:').strip()
       if not n_cod.isnumeric():
         print("Informe apenas números!")
       else:
          dado['cod'] = n_cod
          print('Alteração realizada com sucesso!')
         
    elif(op.upper() == dado['produto']):
       n_prod = input('2 - Novo produto:').strip()
       if (n_prod!= ''):
        dado['produto'] = n_prod
        print('Alteração realizada com sucesso!')
        menu()
       else:
         print('Produto não encontrado.')
         return False 
       
