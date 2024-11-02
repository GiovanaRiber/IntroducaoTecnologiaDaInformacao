#!/usr/bin/env python
# coding: utf-8

# In[2]:

valor_a = 480.5
valor_b = 472.5

# In[3]:

if valor_a > valor_b:
  print(valor_a)

# In[4]:

meuDinheiro = 2.50
precoCoxinha = 2

if meuDinheiro > precoCoxinha:
  print("Vou comer uma coxinha e ainda vai sobrar dinheiro!")
if meuDinheiro == precoCoxinha:
  print("Será que eu devo gastar todo meu dinheiro em uma coxinha?")

print("Com fome ou não, vida que segue")

# In[5]:

fome = True

if fome:
  print('Preciso comer!')
else:
  print('Estou de barriga cheia :)')

# In[6]:

horario_sofia = 20
horario_marco = 21
horario_victor = 19
meu_horario = 20

sofia_disponivel = horario_sofia == meu_horario
marco_disponivel = horario_marco == meu_horario
victor_disponivel = horario_victor == meu_horario

if sofia_disponivel and marco_disponivel and victor_disponivel:
  print("Vamos poder jogar!")
else:
  print("Não vamos poder jogar :(")
# In[7]:

carteira = 2
coxinha = 4
pastel = 3

if carteira >= coxinha:
  print('Vou comprar uma coxinha!')
  carteira = carteira - coxinha

elif carteira >= pastel:
  print('Vou comprar um pastel!')
  carteira = carteira - pastel

else:
  print('Afs, vou passar fome :(')
  print("No final tenho: R$", carteira)

# In[8]:

palavra = 'Morango'

if len(palavra) < 5:
  print("Tem menos de 5 letras")
elif len(palavra) == 5:
  print("Tem exatamente 5 letras")
else:
  print("Tem mais que 5 letras")

# In[9]:

a = 1
b = 5
c = 0.5

if a <= b:
  if a > c:
    print('Primeiro "if" aninhado é verdadeiro')
  else:
    print('Primeiro "if" aninhado é falso')
else:
  print('Primeiro "if" é falso')

# In[10]:

carteira = 60

passagem = 8
bilhete = 30
pipoca = 20
refri = 10

eh_final_de_semana = True

if carteira >= (passagem + bilhete) and eh_final_de_semana:
  print("Vou ao cinema!")

  carteira = carteira - passagem - bilhete
  print("Ainda tenho", carteira)

  if carteira >= (pipoca + refri):
    print("Irei comer pipoca com refri :D")

  elif carteira >= pipoca or carteira >= refri:
    print("Não consigo comprar os dois. Vou comprar só um :/")

  else:
    print("Cinema é pra ver filme. Não preciso de comida :|")

elif not eh_final_de_semana:
  print("Hoje não é final de semana, tenho que estudar. Não vou poder ir ao cinema :(")

else:
  print("Não tenho dinheiro suficiente. Não vou poder ir ao cinema :(")

# In[11]:

n1 = 2
n2 = 1
n3 = 4

maior = n1

if n2 > maior:
  print("O maior é", n2)

if n3 > maior :
  print("O maior é", n3)

if n1 == n2 or n2 == n3 or n1 == n3:
  print("Existem pelo menos dois valores iguais")

# In[12]:

nome = 'joao'
senha = 'senha123456'
idade = 18

if len(nome) >= 4:
  print("O nome de usuáio é válido")
else:
  print("O nome de usuáio inválido")

if len(senha) >= 8:
  print("A senha é válida")
else:
  print("A senha inválida")

if idade >= 15:
  print("Idade mínima alcançada")
else:
  print("Infelizme não possui a idade mínima necessária")

# In[13]:

palavra = input("Qual a palavra a ser decifrada? ")
palavra = palavra.strip().lower()
chute = input("Chute uma palavra: ")
chute = chute.strip().lower()

acertou = palavra == chute

if acertou:
  print("Você acertou!")

else:
  print("Chute incorreto!")

# In[14]:

dificuldade = int(input("Escolha a dificuldade (de 1 a 10): "))
tentativas_possiveis = 11 - dificuldade

if dificuldade > 10 or dificuldade < 1:
  quit()

else:

  palavra = input("Qual a palavra a ser decifrada? ")
  palavra = palavra.strip().lower()
  chute = input("Chute uma palavra: ")
  chute = chute.strip().lower()

  acertou = palavra == chute
  if acertou:
    print("Você acertou!")
  else:
    print("Chute incorreto!")

# In[ ]:

print("Exercício 1\n")

a = int(input())
b = int(input())

maior = a

if b > maior:
  maior = b

print("\nO maior valor é", maior)

# In[1]:

print("Exercício 2\n")

palavra = 'Morango'

if len(palavra) < 5:
  print("Tem menos de 5 letras")
elif len(palavra) == 5:
  print("Tem exatamente 5 letras")
else:
  print("Tem mais que 5 letras")
# In[ ]:

print("Exercício 3\n")

n1 = 2
n2 = 4
n3 = 4

maior = n1

if n2 > maior:
  maior = n2

if n3 > maior :
  maior = n3

print("O maior valor é", maior)

if n1 == n2 or n2 == n3 or n1 == n3:
  print("\nExistem pelo menos dois valores iguais")
# In[ ]:

print("Exercício 4\n")

nome = 'joao'
senha = 'senha123456'
idade = 18

if len(nome) >= 4:
  print("O nome de usuáio é válido")
else:
  print("O nome de usuáio inválido")

if len(senha) >= 8:
  print("A senha é válida")
else:
  print("A senha inválida")

if idade >= 15:
  print("Idade válida")
else:
  print("Infelizmente você não possui a idade mínima necessária")