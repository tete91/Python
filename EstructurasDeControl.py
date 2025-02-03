#Vamos a devolver si un numero es par o impar
"""print("Introduzca a continuación y le diremos si es par o impar")
numero=input("Introduzca un numero: ")
numero=int(numero)
if numero%2==0:
    print("El numero es par.")
else:
    print("El numero es impar.")"""

#Vamos a comparar 2 numeros y decir cual es mayor.
"""print("Introduzca a continuación 2 numeros y le diremos cual es mayor")
numero1=input("Introduzca el primer numero:")
numero2=input("Introduzca el segundo numero:")
numero1=int(numero1)
numero2=int(numero2)
if numero1>numero2:
    print("El numero mayor es el: ")
    print (numero1)
else:
    print("El numero mayor es el: ")
    print (numero2)"""

#Vamos a comparar 3 numeros y decir cual es el mayor
"""print("A continuación introduzca 3 numeros y le diremos cual es mayor.")
numero1=input("Introduzca el primer numero:")
numero2=input("Introduzca el segundo numero:")
numero3=input("Introduzca el tercer numero:")
numero1=int (numero1)
numero2=int (numero2)
numero3=int (numero3)
if numero1>numero2 and numero1>numero3:
    print("El numero mayor es el:")
    print(numero1)
elif numero2>numero1 and numero2>numero3:
    print("El numero mayor es el numero:")
    print(numero2)
else:
    print("El numero mayor es el numero: ")
    print(numero3)"""
#Vamos a hallar una renta de C*r*t/1200
#Si el tiempo es <=24 meses 5%
#Si el tiempo es <=60 meses 8%
#Si el tiempo es >60 meses 10%
"""print("A continuación introduzca la cantidad de dinero a solicitar y el plazo de amortizacion en meses.")
cSol=input("Cantidad solicitada:")
plazos=input("Meses:")
plazos=int (plazos)
cSol= int (cSol)
if plazos<=24:
    intereses=(cSol*plazos*5)/1200
if plazos>24 and plazos <=60:
    intereses=(cSol*plazos*8)/1200
if plazos>60:
    intereses=(cSol*plazos*10)/1200
cuotas=(cSol+intereses)/plazos
print("Los intereses totales del prestamo son:")
print(intereses)
print("La cuota mensual del prestamo es:")
print(cuotas)"""

#Vamos a ver si un numero es par y multiplo de 3 e imprimirlo por terminal la informacion
#o si es impar y multiplo de 3 o si par pero no multiplo o impar y no multiplo
"""print("A continuación se le solicitará un numero y le diremos si es par o impar y si es multiplo de 3.")
numero=input("Introduzca el numero a consultar:")
numero=int (numero)
if numero%2==0 and numero%3==0:
    print("El numero " , numero , " es par y multiplo de 3")
if numero%2==0 and numero%3!=0:
    print("El numero " , numero , " es par y no es multiplo de 3")
if numero%2!=0 and numero%3==0:
    print("El numero " , numero , " es impar y multiplo de 3")
if numero%2!=0 and numero%3!=0:
    print("El numero " , numero , " es impar y no es multiplo de 3")"""
    
#Se va a subir a los empleados de la siguiente manera: Los que cobre <15000
#se les aumenta el 15%, los que cobren >=15000 el 12%
#Ademas un 1% adicional por cada hijos y si son mujeres un 2% adicional y 
"""print("A continuación introducira su sueldo anual, genero y numero de hijos y le diremos el sueldo con su aumento.")
salario=input("Diganos su salario anual:")
sexo=input("Diganos si es hombre o mujer:")
hijos=input("Diganos la cantidad de hijos:")
salario=int(salario)
hijos=int (hijos)
sexo=sexo.lower
if sexo=="mujer":
    if salario<15000:
        porAumento=15+2+(hijos)*1
        aumento=salario*porAumento/100
        nuevoSalario=salario+aumento
        print("El aumento será de: ", aumento ,"€")
        print("El nuevo salario será de: " , nuevoSalario , "€")
    if salario>=15000:
        porAumento=12+2+(hijos)*1
        aumento=salario*porAumento/100
        nuevoSalario=salario+aumento
        print("El aumento será de: ", aumento ,"€")
        print("El nuevo salario será de: " , nuevoSalario , "€")
else:
    
    if salario<15000:
        porAumento=15+(hijos)*1
        aumento=salario*porAumento/100
        nuevoSalario=salario+aumento
        print("El aumento será de: ", aumento ,"€")
        print("El nuevo salario será de: " , nuevoSalario , "€")
    if salario>=15000:
        porAumento=12+(hijos)*1
        aumento=salario*porAumento/100
        nuevoSalario=salario+aumento
        print("El aumento será de: ", aumento ,"€")
        print("El nuevo salario será de: " , nuevoSalario , "€")
        print("El nuevo salario mensual será de ",nuevoSalario/14,"€ en 14 pagas o de ",nuevoSalario/12,"€ en 12 pagas.")"""

#Con un numero del 1 al 7 diremos a que dia de la semana pertenece.
"""print("A continuación introduzca un numero y le diremos a que dia de la semana pertenece.")
dia=int(input("Introduzca un numero del 1 al 7:"))
if dia==1:
    print("El numero ",dia," pertenece al Lunes.")
elif dia==2:
    print("El numero ",dia," pertenece al Martes.")
elif dia==3:
    print("El numero ",dia," pertenece al Miercoles.")
elif dia==4:
    print("El numero ",dia," pertenece al Jueves.")
elif dia==5:
    print("El numero ",dia," pertenece al Viernes.")
elif dia==6:
    print("El numero ",dia," pertenece al Sabado.")
elif dia==7:
    print("El numero ",dia," pertenece al Domingo.")
else:
    print("El numero ",dia," no pertenece a un dia de la semana.")"""
    
#Con una nota calificarlo de suspenso, aprobado,...etc
"""print("A continuacion introduzca una nota del examen y le diremos su calificacion.")
nota=float(input("Introduzca la nota del exámen:"))
if nota>=0 and nota<5:
    print("Tienes un Suspenso")
elif nota>=5 and nota<6:
    print("Tienes un suficiente")
elif nota>=6 and nota<7:
    print("Tienes un Bien")
elif nota>=7 and nota<9:
    print("Tienes un Notable")
elif nota>=9 and nota<10:
    print("Tienes un Excelente")
elif nota==10:
    print("Tienes un sobresaliente")
else:
    print("La nota introducida no es valida, vuelva a intentarlo")
"""
#Veremos si un numero es divisible por 2,3 o 5
"""print("A continuación introduzca un numero y le diremos si es divisible por 2, 3, 5, alguno, todos o ninguno.")
numero=int(input("Introduzca el numero a comprobar:"))
print("El numero ",numero," es divisible por: ")
if numero%2==0:
    print("2")
if numero%3==0:
    print("3")
if numero%5==0:
    print("5")
if numero%2!=0 and numero%3!=0 and numero%5!=0:
    print("El numero ",numero," no es divisible por 2 ni 3 ni 5.")
"""
#pediremos un numero par y un impar y en caso de error pediremos que vuelvan a comenzar
"""par=int(input("Introduzca un numero par:"))
impar=int(input("Introduzca un numero impar:"))
if par%2==0 and impar%2!=0:
    print("¡Gracias por su colaboración!")
if par%2!=0:
    print("El numero par no es correcto, vuelva a intentarlo.")
if impar%2==0:
    print("El numero impar no es correcto, vuelva a intentarlo.")
"""
#