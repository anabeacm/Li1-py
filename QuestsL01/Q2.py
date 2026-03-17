def convert(seg):
    horas = seg // 3600
    resto = seg % 3600
    
    minutos = resto // 60
    seg_rest = resto % 60
    
    return horas, minutos, seg_rest

def main():
    total_segundos = int(input("Digite o tempo em segundos: "))
    
    h, m, s = convert(total_segundos)
    
    print(f"{h} hora(s), {m} minuto(s) e {s} segundo(s)")

main()