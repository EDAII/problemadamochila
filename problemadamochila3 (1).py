from random import randint
def retornalista(posicaomenor, pesoinicial):
    pesomenorlista=[]
    pesomenorlista.append(posicaomenor)
    pesomenorlista.append(pesoinicial)
    return pesomenorlista         
def encontramenorpeso(A):
    pesoinicial=A[0][2]
    posicao=0
    posicaomenorpeso=0    
    for i in A:
       if(i[2]<pesoinicial):
         pesoinicial=i[2]
         posicaomenorpeso=posicao
       else:
         if(i[2]==pesoinicial and i[1]>A[posicaomenorpeso][1]):
           pesoinicial=i[2]
           posicaomenorpeso=posicao     
       posicao=posicao+1
    return retornalista(posicaomenorpeso,pesoinicial)
def encontramaiorvalor(A):
    posicao=0
    valorinicial=0    
    posicaomaiorvalor=0  
    for i in A:
       if(i[1]>valorinicial):
         valorinicial=i[1]
         posicaomaiorvalor=posicao
       else:
         if(i[1]==valorinicial and i[2]<A[posicaomenorpeso][2]):
           valorinicial=i[1]
           posicaomaiorvalor=posicao     
       posicao=posicao+1
    return retornalista(posicaomaiorvalor,valorinicial)          
def eliminaelemento(A,i):
    b=[]
    for i2 in A:
     if(i2!=A[i]):
       b.append(i2)           
    return b    
                                                                             
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
          else:
            matrizdepesonovo=eliminaelemento(A,pesomenorlista[0])    
print(matrizdepesonovo)            
print(matrizvaltot)   
