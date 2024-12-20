peso = int(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/altura**2

if imc < 18.5:
    print("Abaixo do peso")
elif imc >=18.6 and imc < 24.9:
    print("Peso normal")
elif imc >= 30 and imc < 34.9:
    print("Obesidade grau 1")
elif imc >= 35 and imc < 39.9:
    print("Obesidade grau 2")
elif imc > 40:
    print("Obesidade grau 3 (Mórbida)")
