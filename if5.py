l1 = int(input("Digite o valor de um lado: "))
l2 = int(input("Digite o valor do segundo lado: "))
l3 = int(input("Digite o valor do terceiro lado: "))

if l1 == l2 and l1 == l3:
    print("É equilátero")
elif l1 == l2 and l1 != l3:
    print("É isóceles")
elif l1 != l2 and l1 != l3:
    print("É escaleno")