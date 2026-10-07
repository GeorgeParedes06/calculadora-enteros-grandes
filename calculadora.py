def limpiar_numero(num_str):
    """Elimina espacios y ceros a la izquierda no significativos."""
    num_str = num_str.strip().lstrip("0")
    return num_str if num_str else "0"
def es_menor(num1, num2):
    """Determina si num1 < num2 numéricamente (ambos positivos)."""
    if len(num1) != len(num2):
        return len(num1) < len(num2)
    return num1 < num2
def sumar_enteros_grandes(num1, num2):
    """Suma dos números representados como strings dígito por dígito."""
    num1 = limpiar_numero(num1)
    num2 = limpiar_numero(num2)
    i = len(num1) - 1
    j = len(num2) - 1
    acarreo = 0
    resultado = []
    while i >= 0 or j >= 0 or acarreo:
        d1 = int(num1[i]) if i >= 0 else 0
        d2 = int(num2[j]) if j >= 0 else 0
        
        suma = d1 + d2 + acarreo
        resultado.append(str(suma % 10))
        acarreo = suma // 10
        
        i -= 1
        j -= 1
        
    resultado.reverse()
    return "".join(resultado)

def restar_enteros_grandes(num1, num2):
    """Resta dos números representados como strings dígito por dígito (num1 - num2)."""
    num1 = limpiar_numero(num1)
    num2 = limpiar_numero(num2)
    
    if num1 == num2:
        return "0"
        
    negativo = False
    if es_menor(num1, num2):
        num1, num2 = num2, num1
        negativo = True
        
    i = len(num1) - 1
    j = len(num2) - 1
    prestamo = 0
    resultado = []
    
    while i >= 0:
        d1 = int(num1[i]) - prestamo
        d2 = int(num2[j]) if j >= 0 else 0
        
        if d1 < d2:
            d1 += 10
            prestamo = 1
        else:
            prestamo = 0
            
        resultado.append(str(d1 - d2))
        i -= 1
        j -= 1
        
    resultado.reverse()
    res_str = "".join(resultado).lstrip("0")
    if not res_str:
        res_str = "0"
        
    return f"-{res_str}" if negativo else res_str

def multiplicar_enteros_grandes(num1, num2):
    """Multiplica dos números enteros grandes representados como cadenas."""
    num1 = limpiar_numero(num1)
    num2 = limpiar_numero(num2)
    
    if num1 == "0" or num2 == "0":
        return "0"
        
    n, m = len(num1), len(num2)
    pos = [0] * (n + m)
    
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mult = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            suma = mult + pos[p2]
            
            pos[p2] = suma % 10
            pos[p1] += suma // 10
    inicio = 0
    while inicio < len(pos) and pos[inicio] == 0:
        inicio += 1
        
    return "".join(str(d) for d in pos[inicio:])

def menu():
    while True:
        print("\n=== CALCULADORA DE ENTEROS GRANDES ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "4":
            print("Saliendo del programa...")
            break
            
        if opcion not in ["1", "2", "3"]:
            print("Opción inválida. Intente de nuevo.")
            continue   
        n1 = input("Ingrese el primer número entero grande: ").strip()
        n2 = input("Ingrese el segundo número entero grande: ").strip()
        if not (n1.isdigit() and n2.isdigit()):
            print("Error: Ingrese únicamente números enteros positivos válidos.")
            continue
            
        if opcion == "1":
            print(f"\nResultado (Suma): {sumar_enteros_grandes(n1, n2)}")
        elif opcion == "2":
            print(f"\nResultado (Resta): {restar_enteros_grandes(n1, n2)}")
        elif opcion == "3":
            print(f"\nResultado (Multiplicación): {multiplicar_enteros_grandes(n1, n2)}")

if __name__ == "__main__":
    menu()