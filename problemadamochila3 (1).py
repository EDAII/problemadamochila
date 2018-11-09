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
def setacampovalor(pesomenorlista, i2,i,matrizvaltot,matrizresultado,valor,elemento,valor4):
          valor=0
          i3=pesomenorlista[0][0]     
          ianterior=i-1 
          pesomenor=[]   
          pesomenor.append(pesomenorlista[0][0])
          pesomenor.append(pesomenorlista[1][0])    
          if(i==0 or i2==0):
            return 0
          if(i2<pesomenorlista[0][1]):
             return 0   
          if(pesomenorlista[0][1]<=i2 and i==1):
            valor=valor+matrizresultado[pesomenorlista[0][0]][1]
            i2=i2-pesomenorlista[0][1]        
          else:      
            if(i2==pesomenorlista[0][1]):  
              valor=valor4
              i2=i2-pesomenorlista[0][1]  
            elif(i2>pesomenorlista[0][1] and i2<pesomenorlista[1][1]):
              valorintermediario=retornamaior(pesomenor,matrizresultado)
              i2=i2-valorintermediario[1]
              valor=valor+valorintermediario[0]         
            if(i2==pesomenorlista[1][1]):
               valorlista=[]  
               valorlista=retornamaior(pesomenor,matrizresultado)
               valor=valorlista[0]
               i2=valorlista[1]
            elif(elemento[2]<=i2):
                 i2=i2-elemento[2]
                 valor3=elemento[1]  
                 matrizresultado=eliminaelemento(matrizresultado,elemento)   
                 valor2=setacampovalor(pesomenorlista, i2,i,matrizvaltot,matrizresultado,0,elemento,valor4)   
                 valor=valor+valor3+valor2  
                 print(" este é o valor do setacampo :", valor2)                      
          if(matrizvaltot[ianterior][1]>valor):
            valor=matrizvaltot[ianterior][1]
            i2=0           
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
      print(matrizresultado)
      for i2 in range(d+1):
          pesomenorlista.append(encontramenorpeso(matrizresultado))
          matrizrestante=eliminaelemento(matrizresultado,matrizresultado[pesomenorlista[0][0]])          
          pesomenorlista.append(encontramenorpeso(matrizrestante))      
          i3=pesomenorlista[0][0]       
          matrizvaltot[i][i2]=setacampovalor(pesomenorlista,i2,i,matrizvaltot,matrizresultado,0,matrizresultado[i],matrizresultado[i3][1])       
    print(matrizvaltot)          
main()
