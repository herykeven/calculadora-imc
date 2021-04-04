peso = float(input("Digite seu peso em kilogramas: "))
altura = float(input("Digite sua altura em metros: "))
imc = (peso / (altura * altura))

print (imc)

if imc < 18.5:
    print("Voce esta abaixo do peso.")
elif (imc >= 18.5) and (imc <= 24.9):
    print("Voce esta com o peso saudavel.")
elif (imc >= 25) and (imc <= 29.9):
    print("Voce esta com sobrepeso.")
elif (imc >= 30) and (imc <= 34.9):
    print("Voce esta obeso.")
elif imc >= 35:
    print("Voce esta extremamente obeso.")


