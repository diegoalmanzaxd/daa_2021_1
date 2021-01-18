class NodoArbol:
  def __init__(self,value,left=None,rigth=None):
    self.data=value
    self.left=left
    self.rigth=rigth
    self.ban=0

def recorrido(arb):
    mov=[]
    bandera=0
    lis1=[]#Nodos hoja
    lis2=[]#niveles
    
    while bandera==0:
        bandera2=0
        aux=arb
        for i in mov:
            if i=="L":
                aux=aux.left
            if i=="R":
                aux=aux.rigth
        if len(mov)==0 and arb.left.ban==1 and arb.rigth.ban==1:
            bandera=1
        if len(mov)==0 and arb.left==None and arb.rigth==None:
            bandera=1
        if aux.left!= None and aux.left.ban==0 and bandera2==0:
            aux=aux.left
            aux.ban=1
            mov.append("L")
            bandera2=1
        if aux.rigth!=None and aux.rigth.ban==0 and bandera2==0:
            aux=aux.rigth
            aux.ban=1
            mov.append("R")
            bandera2=1
        if aux.rigth==None and aux.left==None:
            lis1.append(aux.data)
            lis2.append(len(mov))
            mov.pop()
        if aux.left!=None and aux.rigth!=None and aux!=arb:
            if aux.left.ban==1 and aux.rigth.ban==1:
                mov.pop()
        if aux.rigth!=None:        
            if aux.left==None and aux.rigth.ban==1:
                mov.pop()
        if aux.left!=None:
            if aux.left.ban==1 and aux.rigth==None:
                mov.pop()
    for i in range(len(lis2)-1):
      for j in range(i):
        if lis2[j]>lis2[j+1]:
          aux=lis1[j]
          lis1[j]=lis1[j+1]
          lis1[j+1]=aux
          aux2=lis2[j]
          lis2[j]=lis2[j+1]
          lis2[j+1]=aux2
    print("----------------------------------------------------------------")
    for i in range(len(lis2)):
      if lis2[i]==lis2[len(lis2)-1]:
        print("Nodo",lis1[i],"en el nivel",lis2[i])
    print("----------------------------------------------------------------")  

def main():
    A=NodoArbol("JUAN",NodoArbol("ALDOLFO",NodoArbol("KARIME"),NodoArbol("FERNANDA",NodoArbol("JAVIER"),NodoArbol("GILIBERTO"))),NodoArbol("ANTUAN",None,NodoArbol("TOBIAS",NodoArbol("ANDREW"))))
    B=NodoArbol("5",NodoArbol("4",NodoArbol("9",NodoArbol(None,NodoArbol("7"))),NodoArbol("110")),NodoArbol("50",NodoArbol("65",NodoArbol(None,NodoArbol("69"))),NodoArbol("44",NodoArbol("99"),NodoArbol("100"))))
    C=NodoArbol("A",NodoArbol("X",NodoArbol("M"),NodoArbol("B")),NodoArbol("S",NodoArbol("P")))
    D=NodoArbol("21",NodoArbol("50",NodoArbol("44"),NodoArbol("8")),NodoArbol("80",NodoArbol("62"),NodoArbol("14")))
    recorrido(A)
    recorrido(B)
    recorrido(C)
    recorrido(D)
main()
