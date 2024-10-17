
#introducir datos:
Xo=float(input("determine la posición inicial en metros"))
T=float(input("determine el tiempo en segundos"))
Vo=float(input("determine la velocidad inicial en m/s"))
a=float(input("determine la aceleración en m/s**"))

#Calcular la posición final del objeto
Xf= Xo + Vo*T + 0.5 * a * T **2
print ("la posición final es:", Xf )

#Calcular la velocidad del objeto
velocidad=Vo + a * T
print  ("la velocidad es:", velocidad )


#Print aceleración
print ("la aceleración es:", a)