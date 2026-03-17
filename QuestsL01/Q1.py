def ler_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    return n1, n2, n3

def calcular_media(n1, n2, n3):
    pesos = (2, 3, 5)
    notas_ponderadas = (n1 * pesos[0]) + (n2 * pesos[1]) + (n3 * pesos[2])
    media = notas_ponderadas / sum(pesos)
    return media

def main():
    n1, n2, n3 = ler_notas()
    media = calcular_media(n1, n2, n3)
    print(f"A média final do aluno é: {media:.2f}")

main()