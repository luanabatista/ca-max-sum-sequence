# Universidade Federal do Sul e Sudeste do Pará
# Complexidade de Algoritmos - Prova 2 Parte 2
# Alunos: Luana Batista e José Arthur 

import random
import sys
import time

################# Função Criar Array ################
def criarArray(n):
   array = []
   for x in range(n):
      array.append(random.randint(-30, 30))
   return array

#################### Algoritmo 1 ####################
def altura1(v):
   n = len(v)
   smax = v[0]
   for i in range(n):
      for k in range(i, n):
         s = 0
         for j in range(i, k+1):
            s += v[j]
            if s > smax:
               smax = s
   return smax

#################### Algoritmo 2 ####################
def altura2(v):
   n = len(v)
   smax = v[0]
   for q in range(n):
      s = 0
      for j in range(q, n):
         s += v[j]
         if s > smax:
            smax = s
   return smax

def valorMax(v):
   i = v[0]
   for n in v:
      if n > i:
         i = n
   return i

#################### Algoritmo 3 ####################
def altura3(v, ini, fim):
   # se o array contem 1 elemento
   if ini == fim:
      # retorna o próprio elemento
      return v[ini]
   
   # encontra o elemento do meio no array
   meio = (ini + fim)//2

   # recursivamente encontra a soma de segmento máximo 
   # entre o lado esquerdo e direito do array 
   x1 = altura3(v, ini, meio)
   x2 = altura3(v, meio+1, fim)

   # encontra a soma de segmento máximo no lado esquerdo 
   # do array, incluindo o elemento do meio
   y1 = -sys.maxsize
   s = 0
   for i in range(meio, ini-1, -1):
      s += v[i]
      if s > y1:
         y1 = s

   # encontra a soma de segmento máximo no lado direito 
   # do array, excluindo o elemento do meio
   y2 = -sys.maxsize
   s = 0 
   for j in range(meio+1, fim+1):
      s += v[j]
      if s > y2:
         y2 = s
      
   # atribui a smax o maior valor entre o lado esquerdo, 
   # o lado direito ou a soma dos dois lados
   smax = valorMax([int(x1), int(x2), int(y1+y2)])
   return smax

#################### Algoritmo 4 ####################
def altura4(v):
   n = len(v)
   
   s = 0
   smax = v[0]
   for j in range(n):
      if s < 0:
         s = v[j]
      else:
         s += v[j]
      if s > smax:
         smax = s
   return smax

############### Execução do Programa #################
v = criarArray(int(input("Digite o tamanho do array: ")))
print(f"Array: {v}")

tinicial = time.perf_counter()
print(f"\nAlgoritmo 4 (Θ(n)): {altura4(v)}")
tfinal = time.perf_counter()
print("Tempo de execução: {:.6f}".format(tfinal-tinicial))

tinicial = time.perf_counter()
print(f"\nAlgoritmo 3 (Θ(nLogn)): {altura3(v, 0, len(v)-1)}")
tfinal = time.perf_counter()
print("Tempo de execução: {:.6f}".format(tfinal-tinicial))

tinicial = time.perf_counter()
print(f"\nAlgoritmo 2 (Θ(n²)): {altura2(v)}")
tfinal = time.perf_counter()
print("Tempo de execução: {:.6f}".format(tfinal-tinicial))

tinicial = time.perf_counter()
print(f"\nAlgoritmo 1 (Θ(n³)): {altura1(v)}")
tfinal = time.perf_counter()
print("Tempo de execução: {:.6f}".format(tfinal-tinicial))

