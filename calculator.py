def calcular(expresion):
    try:
        # Evalúa la expresión matemática
        resultado = eval(expresion)
        return resultado
    except ZeroDivisionError:
        return "Error: División entre cero."
    except SyntaxError:
        return "Error: Expresión no válida."
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Calculadora")
    print("Instrucciones:")
    print("- Ingresa una expresión matemática (por ejemplo, 3 + 5 * 2).")
    print("- Operaciones soportadas: +, -, *, /, ** (potencia).")
    print("- Escribe 'salir' para terminar.")

    while True:
        expresion = input("\nIngresa una expresión: ").strip()

        if expresion.lower() == "salir":
            print("¡Gracias por usar la calculadora!")
            break

        if not expresion:
            print("Por favor, ingresa una expresión.")
            continue

        resultado = calcular(expresion)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
