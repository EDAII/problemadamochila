from random import randint
def retornalista(posicaomenor, pesoinicial):
    pesomenorlista=[]
    pesomenorlista.append(posicaomenor)
    pesomenorlista.append(pesoinicial)
    return pesomenorlista         
def encontramenorpeso(A):
    pesoinicial=100# chutado um peso esdruxulo de alto    
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
def retornamaior(pesomenor,A):
   result=[] 
   i=pesomenor[0]
   i2=pesomenor[1]     
   if(A[i][1]>A[i2][1]):
      result.append(A[i][1])
      result.append(i2-A[i][2])  
   else:
      result.append(A[i2][1]) 
      result.append(i2-A[i2][2])
   return result          
def setacampovalor(pesomenorlista,i,matrizvaltot,matrizresultado,elemento,valor4,resultado,i2):
          valor=0    
          ianterior=i-1 
          pesomenor=[]   
          pesomenor.append(pesomenorlista[0][0])
          pesomenor.append(pesomenorlista[1][0])
          valorlista=[]
          usada=[]   
          i2=resultado[0]         
          if(i==0 or i2==0):
            resultado.append(0)
            resultado.append(0)
            return resultado 
          if(i2<pesomenorlista[0][1]):
             valorlista.append(0)
             usada.append(0)        
          if(pesomenorlista[0][1]<=i2 and i==1):
            resultado.append(matrizresultado[pesomenor[0]][1])
            resultado.append(pesomenorlista[0][1])
            return resultado                               
          if(i2>=pesomenorlista[0][1]):
              i5=pesomenor[0] - 1   
              valor12=matrizresultado[i5][1]   
              valorlista.append(valor12)
              usada.append(pesomenorlista[0][1])      
          if(i2>=pesomenorlista[1][1]):
              valor11=matrizresultado[pesomenor[1]][1] 
              valorlista.append(valor11)
              usada.append(pesomenorlista[1][1])     
          if(elemento[2]<=i2):
                 usada.append(elemento[2]) 
                 resultado[0]=resultado[0]-elemento[2]       
                 valor3=elemento[1]  
                 matrizresultado=eliminaelemento(matrizresultado,elemento)   
                 valorlista.append(setacampovalor(pesomenorlista,i,matrizvaltot,matrizresultado,elemento,valor4, resultado,i2)[1])        
          valorlista.append(matrizvaltot[ianterior][i2])   
          valor=valorlista[0]
          posicao=0
          for valort in valorlista:   
               if(valort>valor):     
                 valor=valort   
          posicao=posicao+1 
          usada.append(resultado[0])     
          resultado[0]=resultado[0]-usada[posicao]  
          resultado[1]=resultado[1]+valor                                              
          return resultado             
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
      print(matrizresultado)
      for i2 in range(d+1):
          pesomenorlista.append(encontramenorpeso(matrizresultado))
          matrizrestante=eliminaelemento(matrizresultado,matrizresultado[pesomenorlista[0][0]])          
          pesomenorlista.append(encontramenorpeso(matrizrestante))      
          i3=pesomenorlista[0][0]
          resultado=[]
          resultado2=[]      
          resultado.append(i2)
          resultado.append(0)                 
          resultado2=setacampovalor(pesomenorlista,i,matrizvaltot,matrizresultado,matrizresultado[i],matrizresultado[i3][1], resultado,i2)   
          matrizvaltot[i][i2]=resultado2[1]        
    print(matrizvaltot)          
main()
