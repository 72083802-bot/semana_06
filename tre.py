print("dime lo que sea")
lo_que_sea = input()
print("Hmm... ", lo_que_sea, "... ¿en serio? ")
#la funcion input() con un argumento
lo_que_sea = input("dime lo que sea: ")
print("Hmm... ", lo_que_sea, "... ¿en serio? ")

numero = int(input("ingresa un numero: "))
resultado = numero ** 2.0
print (numero, "al cuadrado es", resultado)
#calcular hipotenusa 

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#OPERADORES CADENA
Text1 = "ALEXANDER"
Text2 = "PAPULEX"
print(Text1 * Text2)

fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")