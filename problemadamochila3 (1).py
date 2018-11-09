from random import randint
def retornalista(posicaomenor, pesoinicial):
    pesomenorlista=[]
    pesomenorlista.append(posicaomenor)
    pesomenorlista.append(pesoinicial)
    return pesomenorlista         
def encontramenorpeso(A):
    pesoinicial=100
    posicao=0
    posicaomenorpeso=0# chutado um peso esdruxulo de alto    
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
     if(i2!=i):
       b.append(i2)           
    return b 
def selecionatamanho( A,i2):
    b=[]
    posicao=0      
    for Aele in A:
      if(posicao<=i2):
        b.append(Aele)
      posicao=posicao+1
    return b 
def retornamaior( i , i2,A):
    if(A[i][1]>A[i2][1]):
      return A[i][1]
    else:
      return A[i2][1]   
def setacampovalor(pesomenorlista, i2,i,matrizvaltot,matrizresultado,valor):
          valor=0
          if(i==0 or i2==0):
            valor=0
          if(pesomenorlista[0][1]<=i2 and i==1):
            valor=valor+matrizresultado[pesomenorlista[0][0]][1]     
          else:      
            if(i2==pesomenorlista[0][1]):
              valor=valor+matrizresultado[pesomenorlista[0][0]][1] 
            elif(i2==pesomenorlista[0][1]):
              print(pesomenorlista[1][0])
              if(i2==pesomenorlista[1][1]):
                 valor=valor+retornamior(pesomenorlista[0][0],pesomenorlista[1][0])                  
            elif(len(pesomenorlista)>=2):   
                if(i2>pesomenorlista[0][1] and i2<pesomenorlista[1][1]):
                    valor=valor+matrizresultado[pesomenorlista[0][0]][1]  
          return valor             
def main():                                                                             
    a=input("Digite a quantidade de elementos")
    A=[]
    colunas=int(a)+1
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
    matrizresultado=[] 
    for i in range(colunas):
      matrizvaltot.append([0]*(d+1))  
      pesomenorlista=[]
      matrizresultado=selecionatamanho(A,i)
      for i2 in range(d+1):
          pesomenorlista.append(encontramenorpeso(matrizresultado))
          matrizrestante=eliminaelemento(matrizresultado,matrizresultado[pesomenorlista[0][0]])          
          pesomenorlista.append(encontramenorpeso(matrizrestante))      
          matrizvaltot[i][i2]=setacampovalor(pesomenorlista,i2,i,matrizvaltot,matrizresultado,0)  
          print(" este e o primeiro elemento da lista:",pesomenorlista[0][0])  
    print(matrizvaltot)          
main()
