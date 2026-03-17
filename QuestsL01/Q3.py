def calc_custof(c_fab):
    distribuidor = c_fab * 0.28
    impostos = c_fab * 0.45
    return c_fab + distribuidor + impostos

def main():
    c_fab = float(input("Digite o custo de fábrica: "))
    
    custof = calc_custof(c_fab)
    
    print(f"Custo ao consumidor: R$ {custof:.2f}")

main()