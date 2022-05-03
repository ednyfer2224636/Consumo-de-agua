"""Calcular el gasto de agua de una viviendo dado el # de metros cúbicos gastados"""

x = float(input("Digite el número de metros cúbicos consumidos: "))

v = float(x + 10000)

if x <= 50:
    v = 10000
    print("El gasto de agua en su vivienda es", v)

elif x > 50 and x <= 200:
    v = float(((x-50) * 2000) + 10000)
    print("El gasto de agua en su vivienda es", v)

elif x > 200:
        v = float((3000*(x-200)) +(2000*150)+ 10000)
        print("El gasto de agua en su vivienda es", v)
    
else: 
    print("Ahorre agua")

