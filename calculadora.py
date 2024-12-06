import math

def exibir_menu():
    print("\n=== Calculadora Python ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")

def realizar_operacao(opcao):
    if opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    
    if opcao == 1:
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif opcao == 2:
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif opcao == 3:
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif opcao == 4:
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: Divisão por zero.")
    elif opcao == 5:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        print(f"Resultado: {base} ^ {expoente} = {math.pow(base, expoente)}")
    elif opcao == 6:
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        if num >= 0:
            print(f"Resultado: √{num} = {math.sqrt(num)}")
        else:
            print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")

def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 7:
            print("Saindo da calculadora. Até mais!")
            break
        elif 1 <= opcao <= 6:
            realizar_operacao(opcao)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
