from random import randint

def encontramenorpeso(matrizpesoval):
      pesoinicial=matrizpesoval[0][2]
      posic=0
      pesomenor=[]
      pesomenor.append(pesoinicial)
      pesomenor.append(posic)   
      for i in matrizpesoval:
        if(i[2]<pesoinicial):
          pesoinicial=i[2]
          pesomenor[0]=posic
          pesomenor[1]=pesoinicial 
        else:
          if(i[2]==pesoinicial):
            if(i[1]>matrizpesoval[posic][1]):
               pesoinicial=i[2]
               pesomenor[0]=posic
               pesomenor[1]=pesoinicial                  
        posic=posic+1  
      return   pesomenor
def encontramaiorvalor(matrizpesoval):
      valorinicial=matrizpesoval[0][1]
      posic=0
      maiorvalor=[]
      maiorvalor.append(posic)
      maiorvalor.append(valorinicial)   
      for i in  range(len(matrizpesoval)):
        if(matrizpesoval[i][1]>valorinicial):
          valorinicial=matrizpesoval[i][1]
          maiorvalor[0]=i
          maiorvalor[1]=valorinicial 
        else:
          if(matrizpesoval[i][1]==valorinicial):
            print(" a posição do elemento de maior valor ew:", maiorvalor[0])
            if(matrizpesoval[i][2]<matrizpesoval[maiorvalor[0]][2]):
               valorinicial=matrizpesoval[i][1]
               maiorvalor[0]=i
               print(" o maior valor e:",maiorvalor[1])  
               maiorvalor[1]=valorinicial 
      print("o maior valor e:", maiorvalor[1])                 
      print(" esta e a posicao do elemento:",maiorvalor[0],"\n")    
      return   maiorvalor
def constroialternativa(i2,A):
     valor=0  
     print("www")
     resultvalor=encontramaiorvalor(A)
     if(A[resultvalor[0]][2]<=i2):
       valor=resultvalor[0]
       capacidade=i2-A[resultvalor[0]][2]
       print(" a capacidade que falta e:" , capacidade)      
     return valor     
def seleciona(i2,A):  
        canditados=[]
        canditados.append([0]*2)  
        valor=0    
        if(i2==1):
          result=encontramenorpeso(A)        
          if(result[1]==i2):
            posic=result[0] 
            valor=A[posic][1]
          else:
            valor=constroialternativa(i2,A)
            c=len(A)   
            A=selecionaindice(valor,c,A)       
        return valor
def seleciona2(i,A):
      b=[]
      for i2 in range(i):
         b.append(A[i2])
      print(b)    
      return seleciona(i2,b)      
def selecionaindice(i,tamanho,A):
    b=[]   
    for i2 in range(tamanho):
        if (i2!=i):
           b.append(i2)
                                                                                     
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
          matrizvaltot[i][i2]=seleciona2(i,A)   
print(matrizvaltot)   
