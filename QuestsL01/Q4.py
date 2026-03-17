def validar_angulos(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a + b + c != 180:
        return False
    
    return True


def tipo_triangulo(a, b, c):
    if (a == b + c) or (b == a + c) or (c == a + b):
        return "Triângulo Retângulo"
    
    elif (a > b + c) or (b > a + c) or (c > a + b):
        return "Triângulo Obtusângulo"
    
    else:
        return "Triângulo Acutângulo"


def main():
    try:
        a = float(input("Digite o ângulo A: "))
        b = float(input("Digite o ângulo B: "))
        c = float(input("Digite o ângulo C: "))
        
        if validar_angulos(a, b, c):
            print("Os ângulos formam um triângulo.")
            
            tipo = tipo_triangulo(a, b, c)
            print("Tipo:", tipo)
        else:
            print("Os valores informados NÃO formam um triângulo válido.")
    
    except ValueError:
        print("Entrada inválida. Digite apenas números.")


main()