#!/usr/bin/env python
# coding: utf-8

# In[ ]:

contador = 0

while contador <= 6:
  print (contador)
  contador = contador + 1

# In[ ]:

x = 0

while x < 100 and x != 20 :
  print("X está valendo " , x )
  x += 1

print("Saímos do laço")

# In[ ]:

soma_total = 0
media = "Nenhuma média foi calculada"
qtd_notas = 0
calcula_media = True

while calcula_media:
  nota = input("Informe a sua nota: ")

  if nota == ".":
    calcula_media = False

  else:
    soma_total += float(nota)
    qtd_notas += 1

media = soma_total / qtd_notas

print(f"Média: {media}")

# In[ ]:

list(range(1, 5))

# In[ ]:

list(range(0, 9, 2))

# In[ ]:

list(range(10, 0, -1))

# In[ ]:

num = 0
print("Início")

for num in range(1, 5, 1):
  print(num)

print("Fim")

# In[ ]:

N = int(input())

for i in range(0, N + 1, 2):
  if i != 0:
    print(f"{i} é par!")

# In[ ]:

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

# In[ ]:

palavra = input()

for letra in palavra:
  print(letra, end=" ")
print()

# In[ ]:

palavra_string = input().strip().lower()
palavra = []

for letra in palavra_string:
  palavra.append(letra)
palavra

# In[ ]:

palavra_string = input().strip().lower()
palavra = []

for letra in palavra_string:
  palavra.append(letra)
list(set(palavra))

# In[ ]:

chute = str(input()).strip().lower()

if len(chute) > 1:
  print("Isso é problemático!")
else:
  print("Isso é bom!")

# In[ ]:

palavra_string = input().strip().lower()
palavra = []

for letra in palavra_string:
  palavra.append(letra)
palavra = list(set(palavra))

chutes = []
finalizado = False
while not finalizado:
  chute = str(input()).strip().lower()
  if len(chute) > 1:
    print("Isso é problemático!")
  else:
    print("Isso é bom!")
  chutes.append(chute)
  chutes = list(set(chutes))

  falta_letra = False
  for letra in palavra:
    if letra not in chutes:
      print("Faltam letras ainda.")
      falta_letra = True

  if falta_letra:
    continue
  else:
    finalizado = True
    print("Acertou!")

# In[ ]:

palavra_string = input().strip().lower()
palavra = []

for letra in palavra_string:
  palavra.append(letra)
palavra = list(set(palavra))

chutes = []
finalizado = False
while not finalizado:
  chute = str(input()).strip().lower()
  if len(chute) > 1:
    print("Chute UMA LETRA!")
    continue
  chutes.append(chute)
  chutes = list(set(chutes))

  falta_letra = False
  for letra in palavra:
    if letra not in chutes:
      falta_letra = True
    if falta_letra:
      continue
      finalizado = True
      print("Acertou!")

# In[ ]:

dificuldade = int(input("Escolha a dificuldade (de 1 a 10): "))

if dificuldade > 10 or dificuldade < 1:
  quit()

tentativas_possiveis = 11 - dificuldade

palavra_string = input("Qual a palavra a ser decifrada? ").strip().lower()

palavra = []
for letra in palavra_string:
  palavra.append(letra)
palavra = list(set(palavra))

if palavra_string.isalpha():
  print("Pode começar!")
  finalizado = False
else:
  print("Palavra proibida!")
  finalizado = True

chutes = []
while not finalizado and tentativas_possiveis:
  chute = input("Chute uma letra: ").strip().lower()
  if len(chute) > 1:
    print("Chute UMA LETRA!")
    continue

  chutes.append(chute)
  chutes = list(set(chutes))

  falta_letra = False
  for letra in palavra:
    if letra not in chutes:
      falta_letra = True
  if falta_letra:
      if chute not in palavra:
        tentativas_possiveis -= 1
        print("Chute incorreto!")
        print(f"Você pode errar mais {tentativas_possiveis} vezes!")
      else:
        print("Chute correto, ainda faltam letras!")
  else:
    print("Você acertou!")
    finalizado = True

if finalizado and palavra_string.isalpha():
  print(f'A palavra era "{palavra_string}".')

for letra in palavra:
  if letra in chutes:
    print(letra, end=' ')
  else:
    print('_', end=' ')

# In[1]:

dificuldade = int(input("Escolha a dificuldade (de 1 a 10): "))

if dificuldade > 10 or dificuldade < 1:
  quit()

tentativas_possiveis = 11 - dificuldade

palavra_string = input("Qual a palavra a ser decifrada? ").strip().lower()

palavra = []

for letra in palavra_string:
  palavra.append(letra)
palavra = list(set(palavra))

if palavra_string.isalpha():
  print("Pode começar!")
  finalizado = False
else:
  print("Palavra proibida!")
  finalizado = True

chutes = []
while not finalizado and tentativas_possiveis:
  chute = input("Chute uma letra: ").strip().lower()

  if len(chute) > 1:
    print("Chute UMA LETRA!")
    continue

  if chute in chutes:
    print("Chute repetido...")
    continue

  chutes.append(chute)
  chutes = list(set(chutes))

  for letra in palavra_string:
    if letra in chutes:
      print(letra, end=' ')
    else:
      print('_', end=' ')
  print()

  falta_letra = False
  for letra in palavra:
    if letra not in chutes:
        falta_letra = True
  if falta_letra:
      if chute not in palavra:
          tentativas_possiveis -= 1
          print("Chute incorreto!")
          print(f"Você pode errar mais {tentativas_possiveis} vezes!")
      else:
        print("Chute correto, ainda faltam letras!")
  else:
    print("Você acertou!")
    finalizado = True

if finalizado and palavra_string.isalpha():
  print(f'A palavra era "{palavra_string}".')

for letra in palavra:
  if letra in chutes:
    print(letra, end=' ')
  else:
    print('_', end=' ')

# In[ ]:

print("Exercício 1\n")

n = int(input())
m = int(input())

if m % n == 0:
  print(m, "é múltiplo de", n)
else:
  print(m, "não múltiplo de", n)

# In[ ]:

print("Exercício 2\n")
n = int(input())

cont = 0

while cont <= n:
  print(cont)
  cont = cont + 1

# In[2]:

print("Exercício 3\n")
n = int(input())

cont = 1

while cont <= n:
  if cont % 2 == 0:
    print(cont)
  cont = cont + 1

# In[4]:

palavra_string = input().strip().lower()
palavra = []
for letra in palavra_string:
  palavra.append(letra)
list(set(palavra))