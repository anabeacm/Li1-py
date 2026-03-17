def ler_n():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    return n1, n2, n3

def calc_m(n1, n2, n3):
    pesos = (2, 3, 5)
    notas = (n1 * pesos[0]) + (n2 * pesos[1]) + (n3 * pesos[2])
    media = notas / sum(pesos)
    return media

def main():
    n1, n2, n3 = ler_n()
    media = calc_m(n1, n2, n3)
    print(f"A média final do aluno é: {media}")

main()