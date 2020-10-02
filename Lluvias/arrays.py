#Arrego de una dimension
class Array:
    def __init__(self,n):
        self.__n=n
        self.__arreglo=[]
        for i in range(0,n,1):
            self.__arreglo.append(0)
    def length(self):
        return self.__n
    def get_item(self,index):
        return self.__arreglo[index]
    def set_item(self,index,value):
        self.__arreglo[index]=value
    def clearing(self,value):
        for i in range(0,self.__n,1):
            self.__arreglo[i]=value
    def to_string(self):
        print("Tamaño del arreglo=",self.__n)
        print(self.__arreglo)
#Arrego de dos dimension
class Array2D:

    def __init__(self,rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.__arreglo=[]
        for i in range(self.__rows):
            self.__arreglo.append([])
            for j in range(self.__cols):
                self.__arreglo[i].append(0)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,rows,cols):
        return self.__arreglo[rows][cols]

    def set_item(self,rows,cols,value):
        self.__arreglo[rows][cols]=value

    def clearing(self,value):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__arreglo[i][j]=value
    def llenar(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                n=input("Valor en "+str(i)+","+str(j)+": ")
                self.__arreglo[i][j]=n
    def to_string(self):
        for i in range (self.__rows):
            for j in range(self.__cols):
                print(self.__arreglo[i][j],end="\t")
            print()
        
class Array3D:
    def __init__(self,depth,rows,cols):
        self.__depth=depth
        self.__rows=rows
        self.__cols=cols
        self.__arreglo=[[[0 for k in range(cols)] for j in range(rows)]for i in range(depth)]
    
    def get_num_depth(self):
        return self.__depth

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,depth,rows,cols):
        return self.__arreglo[depth][rows][cols]

    def set_item(self,depth,rows,cols,value):
        self.__arreglo[depth][rows][cols]=value

    def clearing(self,value):
        for i in range(self.__depth):
            for j in range(self.__rows):
                for k in range(self.__cols):
                    self.__arreglo[i][j][k]=value

    def to_string(self):
        capa=1
        for layer in self.__arreglo:
            print('----Capa',capa,'----')
            for ren in layer:
                print(ren)
            capa+=1
        print()
                
