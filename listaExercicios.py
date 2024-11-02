#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from math import pi
print("Exercício 1\n")
r = float(input())

s = pi * (r*r)

print(s)

# In[ ]:

from math import sqrt

print("Exercício 2\n")
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
print(x)

# In[ ]:

print("Exercício 3\n")

# In[ ]:

print("Exercício 4\n")
pessoas = int(input("Estão em quantas pessoas? "))
b = int(input("Quantos balões? "))

resto = b % pessoas
b = b - resto
q = b / pessoas

print("\nCada pessoa ficou com" , int(q), "balões")
print("Sobraram", resto, "balões")


# In[ ]:

print("Exercício 5\n")

s = input().lower()
s[0]

# In[ ]:

print("Exercício 6\n")

A = input().lower()
B = input().lower()

if len(A) < 3 or len(B) < 3:
  print("\nImpossível prosseguir")
  quit()
else:
  print(A[0:3]+B[-3:])

# In[ ]:

print("Exercício 7\n")
n = int(input("Informe um valor: "))

cont = 1
div = 0
while cont <= n:
  if n % cont == 0:
    div = div + 1
  cont = cont + 1

if div == 2:
  primo = "Sim"
else:
  primo = "Não"

print(primo)

# In[ ]:

print("Exercício 8\n")
n = int(input())
m = int(input())

cont = 1
while cont <= n:
  if cont % m == 0:
    print(cont)
  cont = cont + 1

# In[ ]:

print("Exercício 9\n")

n = int(input())

cont = 1
a = 1
b = 0

while cont <= n:
  c = a + b
  print(c)
  a = b
  b = c
  cont = cont + 1

# In[8]:

print("Exercício 10\n")

a = int(input())

a = int(str(a) * 1)
aa = int(str(a) * 2)
aaa = int(str(a) * 3)
aaaa = int(str(a) * 4)

N = a + aa + aaa + aaaa
print(N)