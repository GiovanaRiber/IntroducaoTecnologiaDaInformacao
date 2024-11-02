#!/usr/bin/env python
# coding: utf-8

# In[44]:

carrinho = ["tomates", "batatas", "ovos", "pães", "doritão"]
print(carrinho[1])

# In[45]:

'batatas' in carrinho and "laranja" in carrinho

# In[46]:

'maça' in carrinho

# In[47]:

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
impares[0:5]

# In[48]:

impares[0:3]

# In[49]:

impares[3: ]#não é necesspario definir o fim

# In[50]:

impares[0:8:1]

# In[51]:

impares[0:8:2]

# In[52]:

impares[0:8:3]

# In[53]:

impares[0:8:9999]

# In[54]:

impares[::2]

# In[55]:

impares

# In[56]:

impares[-1]

# In[57]:

impares[-2]

# In[58]:

impares[-11]

# In[59]:

impares[4:-3]

# In[60]:

impares[8:0:-2]

# In[61]:

exp2_6 = [1, 2, 4, 8, 16, 32]
print(exp2_6[::-1])

# In[62]:

print("Tamanho do carrinho = ", len(carrinho ))

# In[63]:

carrinho.count("doritão")

# In[64]:

numeros = [1, 2, 3, 4, 5, 6, 7, 7, 8, 10, 11, 11, 11]
print("Ocorrências de 11 em nossa lista:", numeros.count(11))
print("Ocorrências de 7 em nossa lista:", numeros.count(7))

# In[65]:

numeros = [49, 12, 37,  28, 78, 21, 81, 68, 31, 79, 54]
print("Maior número da lista: ", max(numeros))
print("Menor número da lista: ", min(numeros))

# In[66]:

lista_string = ["zata", "Alpha"]
valor_maximo = max(lista_string)
print(valor_maximo)

# In[67]:

carrinho.append("Kisuco")
carrinho.append("açúcar")

print("Carrinho: ", carrinho)

# In[68]:

print("Estou removendo o item: ", carrinho.pop(4) )
print("Carrinho atualizado:" , carrinho )

# In[69]:

print("Estou removendo o item: ", carrinho.pop() )
print("Carrinho atualizado:" , carrinho )

# In[70]:

if "batatas" in carrinho:
  print("Estou removendo as batatas: ", carrinho.remove("batatas") )
print("Carrinho atualizado:" , carrinho )

# In[71]:

numeros_copiados = numeros.copy()

lista_original = [1, 2, 3, 4, 5]
lista_copiada = lista_original
lista_copiada.append(6)
print("Lista original:", lista_original)
print("Lista copiada:", lista_copiada)

# In[72]:

lista_original = [1, 2, 3, 4, 5]
lista_copiada = lista_original.copy()
lista_copiada.append(6)
print("Lista original:", lista_original)
print("Lista copiada:", lista_copiada)

# In[96]:

print("Lista de numeros desordenada:" , numeros)

numeros_copiados.sort()
print("Lista de numeros ordenada:" , numeros_copiados )

# In[98]:

carrinho.append("HotWheels")
carrinho.sort()
print(carrinho)

# In[75]:

carrinho = numeros
for thiago in numeros:
  print(f"{thiago} é meu amigo!")

# In[76]:

print(f"{'João'} é meu amigo!")
print(f"{'Pedro'} é meu amigo!")

# In[77]:

alunos = ["João", "Pedro", "Henrique", "Manoel", "Carlos", "Gabriel"]

alunos_aprovados = 0
for aluno in alunos:
  nota = float(input(f"Qual a nota de {aluno}? "))

  if nota >= 7:
    print(f"{aluno} passou!")
    alunos_aprovados += 1
  else:
    print(f"{aluno} está de final!")
  if alunos_aprovados == 1:
    passou = "passou"
  else:
    passou = "passaram"
print(f"De {len(alunos)}, {alunos_aprovados} {passou} direto.")

# In[78]:

range(1, 5, 1)

# In[79]:

range(1, 5) == range(1, 5, 1)

# In[80]:

list(range(1,5))

# In[81]:

list(range(0, 9, 2))

# In[82]:

list(range(10, 0, -1))

# In[83]:

N = int(input())
intervalo = list(range(0, N + 1, 2))
intervalo[1:]

# In[84]:

N = int(input())

for i in range(0, N + 1, 2):
  if i != 0:
    print(f"{i} é par!")

# In[85]:

lista = []
print("Digite uma sequência de 6 números para adicionar na lista")
for x in range(6):
  lista.append(input(f"{x+1}) "))
print(lista)

# In[105]:

for i in range(25, -11, -1):
  print(i)

# In[87]:

len("Olá, como você está?")

# In[88]:

minha_string = "Sou uma string"
minha_string[2]

# In[89]:

minha_string = "Sou uma string"
minha_string[0:5]

# In[90]:

minha_string = "Sou uma string"
minha_string.split()

# In[91]:

dificuldade = int(input("Escolha a dificuldade (de 1 a 10): "))

if dificuldade > 10 or dificuldade < 1:
  quit()

tentativas_possiveis = 11 - dificuldade

palavra = input("Qual a palavra a ser decifrada? ")
palavra = palavra.strip().lower()

print("Pode começar!")

finalizado = False
while not finalizado and tentativas_possiveis:
  chute = input("Chute uma palavra: ")

  acertou = palavra == chute
  if acertou:
    print("Você acertou!")
    finalizado = True
  else:
    print("Chute incorreto!")

    tentativas_possiveis -= 1
    print(f"Você pode errar mais {tentativas_possiveis} vezes!")

if finalizado:
  print(f'A palavra era "{palavra}".')