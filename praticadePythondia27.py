def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def main():
    while True:
        print("Operações:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Escolha uma operação (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado: ", adicionar(num1, num2))

            elif escolha == '2':
                print("Resultado: ", subtrair(num1, num2))

            elif escolha == '3':
                print("Resultado: ", multiplicar(num1, num2))

            elif escolha == '4':
                print("Resultado: ", dividir(num1, num2))

        elif escolha == '5':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
