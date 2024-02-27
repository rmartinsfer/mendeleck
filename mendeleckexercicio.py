##EXERCICIO MENDELECK
##Aluno: Rai Martins Ferreira
##RA: 23023558
# Solicita o salário integral e converte para float
salarioIntegral:float = float(input("Entre com o Valor do Salario: "))
print(f"Valor do Salario Digitado: {salarioIntegral}")
# Solicita a quantidade de dias trabalhados e converte para int
diasTrabalhados:int = int(input("Entre com a quantidade de dias Trabalhados: "))
print(f"Quantidade de Dias Trabalhados: {diasTrabalhados}")
# Calcula o valor do salário por dia
calculoResult:float = salarioIntegral / 30
# Calcula o salário proporcional
resultado:float = calculoResult * diasTrabalhados
# Imprime o resultado
print(f"O valor proporcional e: {resultado}")

##EM FORMA DE PASSO A PASSO

# 1.Entrada do Salário Total:
#    - Peça ao usuário para inserir o valor total do salário.
#    - Receba essa entrada e armazene-a como um número.

# 2.Exibição do Salário Digitado:
#    - Mostre na tela o valor do salário que foi digitado pelo usuário.

# 3.Entrada dos Dias Trabalhados:
#    - Solicite ao usuário para informar a quantidade de dias trabalhados.
#    - Receba essa entrada e armazene-a como um número inteiro.

# 4.Exibição dos Dias Trabalhados:
#    - Mostre na tela a quantidade de dias trabalhados que foi informada.

# 5.Cálculo do Salário Diário:
#    - Divida o salário total pelo número padrão de dias em um mês (que neste caso é considerado como 30).
#    - Armazene o resultado dessa divisão, que representa o valor do salário por dia.

# 6.Cálculo do Salário Proporcional:
#    - Multiplique o valor do salário diário pela quantidade de dias trabalhados.
#    - Armazene o resultado dessa multiplicação, que representa o salário proporcional aos dias trabalhados.

# 7.Exibição do Resultado:
#    - Mostre na tela o valor do salário proporcional calculado.
