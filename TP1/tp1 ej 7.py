#ejercicio 7
#Un comerciante, el cual tiene un sueldo base, 
# recibe un 10% extra por comisión por cada venta
# que realiza. Realizar un programa que devuelva el dinero 
# que recibirá por comisión luego de 4 ventas y el total de 
# dinero que ganará ese mes, teniendo en cuenta estas ventas 
# y su sueldo base.

sueldo_base = int(input("ingrese sueldo base"))
venta1 = int(input("ingrese primera ganancia"))
venta2 = int(input("ingrese segunda ganancia"))
venta3 = int(input("ingrese tercera ganancia"))
venta4 = int(input("ingrese cuarta ganancia"))
comisión = venta1*0.1 + venta2*0.1 + venta3*0.1 + + venta4*0.1
sueldo_total= sueldo_base + comisión
print("el sueldo total es", sueldo_total, ".")