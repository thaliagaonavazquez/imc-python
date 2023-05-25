peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2)

print("Tu índice de masa corporal (IMC) es: {:.2f}".format(imc))

if imc <= 18.5:
    print("Bajo peso")
elif imc > 18.5 and imc <= 24.9:
    print("peso saludable")
elif imc > 24.9 and imc <= 29.9:
    print("sobrepeso")
else:
    print("Obesidad")
