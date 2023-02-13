#matriz
#vetor x inicial
#equacoes x
#o resultado anterior fica guardado para cálculo de erro
import time

def jacobi(iteracoes,m,tol):
  b = [] #separa respostas em vetor B para melhor entendimento
  for i in range(0,len(m)):
    b.append(m[i][len(m)])
  a = m #separa incognitas em matriz A para melhor entendimento
  for i in range(0,len(m)):
    a[i].pop()
  x = []
  for i in range(len(m)):
    x.append(0)
  aux = []
  for i in range(len(m)):
    aux.append(0)
  #codigo com x, a e b
  xo = []
  for i in range(len(m)):
    xo.append(0)
    
  #passo 1
  k = 0
  #passo 2
  while k<iteracoes:
    #passo 3
    for i in range(0,len(a)):
      somatoria = b[i]
      for j in range(0,len(a)):
        if j==i:
          continue
        somatoria -= a[i][j]*x[j]
      somatoria/= a[i][i]
      aux[i] = somatoria

    for t in range(len(aux)):
      x[t] = aux[t]

    print('Iteração',k+1,':')
    print(x)
    
    #passo 4 - calcula erro
    erro = 0
    for n in range(0,len(x)):
      y = (x[n]-xo[n])/max(x)
      if y<0:
        y = y*-1
      if (erro<y):
        erro = y
    print('Erro:',erro,'\n')

    if erro < tol:
      print('O procedimento foi bem-sucedido')
      print('Resultados:')
      return x
    #passo 5
    k = k+1

    #passo 6
    for l in range(len(x)):
      xo[l] = x[l]
      
  print('Número máximo de iterações excedido')
  print('O procedimento não foi bem-sucedido')
  return x

def teste1():
  print('Exercício 1\n')
  m = [[2.0,1.0,2.0],[1.0,-2.0,-2.0]]
  iteracoes = 6
  tol = 0.1
  x = jacobi(iteracoes,m,tol)
  print(x,'\n')

def teste2():
  print('Exercício 2\n')
  m = [[10.0,-1.0,2.0,0.0,6.0],[-1.0,11.0,-1.0,3.0,25.0],[2.0,-1.0,10.0,-1.0,-11.0],[0.0,3.0,-1.0,8.0,15.0]]
  iteracoes = 10
  tol = 0.1
  x = jacobi(iteracoes,m,tol)
  print(x,'\n')

def exA():
  print('Exercício A\n')
  m = [[3.0,-3.0,1.0,-1.0],[1.0,1.0,0.0,3.0],[1.0,-1.0,3.0,2.0]]
  iteracoes = 150
  tol = 0.1
  inicio = time.time()
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.01
  inicio = time.time()
  m = [[3.0,-3.0,1.0,-1.0],[1.0,1.0,0.0,3.0],[1.0,-1.0,3.0,2.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.001
  inicio = time.time()
  m = [[3.0,-3.0,1.0,-1.0],[1.0,1.0,0.0,3.0],[1.0,-1.0,3.0,2.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')

def exB():
  print('Exercício B\n')
  m = [[2.0,-1.5,3.0,1.0],[4.0,-4.5,5.0,1.0],[-1.0,0.0,2.0,3.0]]
  iteracoes = 30
  tol = 0.1
  inicio = time.time()
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.01
  inicio = time.time()
  m = [[2.0,-1.5,3.0,1.0],[4.0,-4.5,5.0,1.0],[-1.0,0.0,2.0,3.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.001
  inicio = time.time()
  m = [[2.0,-1.5,3.0,1.0],[4.0,-4.5,5.0,1.0],[-1.0,0.0,2.0,3.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')

def exC():
  print('Exercício C\n')
  m = [[2.0,0.0,0.0,0.0,3.0],[1.0,1.5,0.0,0.0,4.5],[0.0,-3.0,0.5,0.0,-6.6],[2.0,-2.0,1.0,1.0,0.8]]
  iteracoes = 10
  tol = 0.1
  inicio = time.time()
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.01
  inicio = time.time()
  m = [[2.0,0.0,0.0,0.0,3.0],[1.0,1.5,0.0,0.0,4.5],[0.0,-3.0,0.5,0.0,-6.6],[2.0,-2.0,1.0,1.0,0.8]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.001
  inicio = time.time()
  m = [[2.0,0.0,0.0,0.0,3.0],[1.0,1.5,0.0,0.0,4.5],[0.0,-3.0,0.5,0.0,-6.6],[2.0,-2.0,1.0,1.0,0.8]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')

def exD():
  print('Exercício C\n')
  m = [[1.0,1.0,0.0,1.0,2.0],[2.0,1.0,-1.0,1.0,1.0],[4.0,-1.0,-2.0,2.0,0.0],[3.0,-1.0,-1.0,2.0,-3.0]]
  iteracoes = 10000
  tol = 0.01
  inicio = time.time()
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.01
  inicio = time.time()
  m = [[1.0,1.0,0.0,1.0,2.0],[2.0,1.0,-1.0,1.0,1.0],[4.0,-1.0,-2.0,2.0,0.0],[3.0,-1.0,-1.0,2.0,-3.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')
  
  tol = 0.001
  inicio = time.time()
  m = [[1.0,1.0,0.0,1.0,2.0],[2.0,1.0,-1.0,1.0,1.0],[4.0,-1.0,-2.0,2.0,0.0],[3.0,-1.0,-1.0,2.0,-3.0]]
  x = jacobi(iteracoes,m,tol)
  fim = time.time()
  print(x,'\n')
  print('Tempo:', fim-inicio)
  print(x,'\n')

  

teste1()
print('\n')
teste2()

#exA()
#exB()
#exC()
#exD()
