# def contarvogais():
#     palavra = input("Digite uma palavra: ").lower() #serve para tornar a palavra inteira em minúscula

    # vogais = "aeiou"
    # contador = 0

#   for letra in palavra:
#     if letra in vogais: 
#         contador += 1

#   print(f"A palavra digitada {palavra} possui {contador} vogais")

# contarvogais()

def contarvogais():
    palavra = input("Digite uma palavra: ").lower()  # Corrigido para aplicar o método .lower()

    vogais = "aeiou"
    contador = 0

    for letra in palavra:
        if letra in vogais:  # Verifica se a letra é uma vogal
            contador += 1

    print(f"A palavra digitada {palavra} possui {contador} vogais")  # Corrigido para imprimir o contador

contarvogais()