
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
 try:
   codigo =input("Insira o código do produto: ")
   if(codigo.isnumeric() == False):
    print('Informe um número válido!')
    menu()
   else:
    nome = input("Insira o produto: ")
    
    dados_produtos = {
    'cod': codigo,
    'produto': nome.upper()
    }
    dados_all.append(dados_produtos)
    print(dados_all)
    print('Cadastro realizado com sucesso!')
 except ValueError:
   print('Informe apenas números')

   return menu()
#
def listar():
 if (len(dados_all)> 0):
   #for i, item in enumerate(dados_all):
    #print(i, item);
    for item in dados_all:
      print(item)
    return True    
 else:
    print('Não existem produtos cadastrados')
    return False
#
def excluir():
  if listar() == True: 
   op = input('Qual produto deseja excluir?\n')
   
   try:
    for i, dado in enumerate(dados_all):
      if (op == dado['cod']):
       dados_all.remove(dado)
       print('produto excluído com sucesso!')
   except SystemError:
     print('Entre em contato com o suporte')
  else:
    #print('Lote inexistente')
    menu()  
#
def editar():
  if listar() == True: 
   op = input('Qual produto deseja editar?\n')
  try:
    for i, dado in enumerate(dados_all):
      if((op == dado['cod']) or (op.upper() == dado['produto'])):
       n_cod = int(input(print('1 - Editar código do produto:')))
       n_prod = input(print('2 - Editar produto:'))
       if (n_cod !=0) or (n_prod!= ''):
         dado['cod'] = n_cod
         dado['produto'] = n_prod

         print('Alteração realizada com sucesso!')
         menu()
       else:
         print('Verifique os campos')
  except SystemError:
     print('Entre em contato com o suporte')
  else:
    print('Não há produtos')
    menu()




  

