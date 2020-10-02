import xlrd
from arrays import Array3D
def main():
    a3=Array3D(2,33,14)
    for anio in range(2017,2019):
        ruta='./Precipitacion/'+str(anio)+'Precip.xls'
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,34):
            for c in range(0,14):
                a3.set_item(anio-2017,r-1,c,hoja.cell_value(r,c))
     
    a=int(input('Año (2017 o 2018): '))
    e=int(input('Edo (1-32): '))
    m=int(input('Mes (1-12): '))
    print('En',a3.get_item(0,e,0),'hubo un promedio de',round(a3.get_item(a-2017,e,m),2),'en el mes de',a3.get_item(0,0,m))

    promedio=0
    for mes in range(1,13):
        promedio+=a3.get_item(a-2017,e,mes)
    print('El promedio para',a3.get_item(0,e,0),'en',a,'es:',round(promedio/12,2))
    print('El total de lluvias en',a3.get_item(0,e,0),'en',a,'fue:',round(promedio,2))
    mayor=0
    fecha=[0,0,0]
    for a in range(2):
        for e in range(1,33):
            for m in range(1,13):
                aux=int(a3.get_item(a,e,m))
                if aux>mayor:
                    mayor=aux
                    fecha[0]=a
                    fecha[1]=e
                    fecha[2]=m
    print('El mes más lluvioso fue',a3.get_item(0,0,fecha[2]) ,'en ',a3.get_item(0,fecha[1],0),'con ', round(a3.get_item(fecha[0],fecha[1],fecha[2]),2),'en el año',fecha[0]+2017)
    mayor=10000000
    fecha=[0,0,0]
    for a in range(2):
        for e in range(1,33):
            for m in range(1,13):
                aux=float(a3.get_item(a,e,m))
                if aux<mayor:
                    mayor=aux
                    fecha[0]=a
                    fecha[1]=e
                    fecha[2]=m
    print('El mes menos lluvioso fue',a3.get_item(0,0,fecha[2]) ,'en ',a3.get_item(0,fecha[1],0),'con ', a3.get_item(fecha[0],fecha[1],fecha[2]),'en el año',fecha[0]+2017)
   
main()
