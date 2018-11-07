from random import randint

def encontramenorpeso(A):
    pesoinicial=A[0][2]
    posicao=0
    posicaomenorpeso=0    
    for i in A:
       if(i[2]<pesoinicial):
         pesoinicial=i[2]
         posicaomenorpeso=posicao
       posicao=posicao+1
    pesomenorlista=[]
    pesomenorlista.append(posicaomenorpeso)
    pesomenorlista.append(pesoinicial)
    return pesomenorlista              
                                                                                     
a=input("Digite a quantidade de elementos")
A=[]
colunas=int(a)
c=input("Digite a capacidade da mochila")
d=int(c)      
for i in range(colunas):
   valor=randint(1,100)
   peso=randint(1,d)  
   A.append([0]*3)
   A[i][0]=i+1
   A[i][1]=valor
   A[i][2]=peso 
print(A) 
matrizvaltot=[]
for i in range(colunas+1):
    matrizvaltot.append([0]*(d+1))  
    for i2 in range(d+1):
        if(i==0 or i2==0):
          matrizvaltot[i][i2]=0
        else: 
          pesomenorlista=encontramenorpeso(A)
          if(i2==pesomenorlista[1]):
            matrizvaltot[i][i2]=A[pesomenorlista[0]][1]         
print(matrizvaltot)   
