# Leitura das notas
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

# Cálculo da média ponderada
notas = (n1 * 2) + (n2 * 3) + (n3 * 5)
calcMedia = notas / 10

# Exibição do resultado
print("A média final do aluno é:", calcMedia)