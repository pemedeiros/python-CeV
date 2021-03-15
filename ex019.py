import random
n1 = input('Qual o nome do primeiro aluno?')
n2 = input('Qual o nome do segundo aluno?')
n3 = input('Qual o nome do terceiro aluno?')
n4 = input('Qual o nome do quarto aluno?')
#nome = str
#if(num == 1):
 #   nome = n1
  #  print(nome)
#if (num == 2):
  #  nome = n2
  #  print(nome)
#if (num == 3):
 #   nome = n3
#    print(nome)
#if (num == 4):
   # nome = n4
   # print(nome)
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(escolhido)




