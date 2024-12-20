prova = int(input("Digite a nota da prova: "))
atividade = int(input("Digite a nota das atividades: "))
trabalho = int(input("Digite a noto do trabalho: "))

media = (prova + atividade + trabalho) / 3

print(f"{media:.1f}") #usado para limitar a aparição de muitos caracteres em uma dízima

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 6.9:
    print("recuperação")
else:
    print("Reprovado")
