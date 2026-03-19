
import funcoes as f

menu = True

while(menu):
 f.menu()
 op =int(input())
 try:
  if(op== 1):
   f.cadastro()
  elif(op == 2):
   f.listar()
 #print(f"Cliente: {l_lote}")
  elif(op == 3):
   f.excluir()
  elif(op == 4):
   f.menu()
  elif(op==5):
   f.editar()
  elif(op == 0):
   print('Obrigada por utilizar nosso programa. Até a próxima! :)')
   menu = False
 except ValueError:
  print("Opção inválida!")
  

   
    
  

