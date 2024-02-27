ht : float = float(input("Digite Horas Trabalhadas: "))
sh : float = float(input("Digitar Salario Hora: "))

#CALCULAR SALARIO BRUTO
sb : float = ht * sh

discontoAposentadoria: float = sb * 10/ 100

salarioIntermediario : float = sb - discontoAposentadoria
ir : float = salarioIntermediario * 5 /100
sl : float = salarioIntermediario - ir

print("SALARIO BRUTO: ",format(sb, "10.2f"))
print("SALARIO LIQUIDO: ",format(sl, "10.2f"))

##///EXERCICIO 2
peso : float = float(input("Digite seu Peso: "))
altura : float = float(input("Digite a Altura: "))

imc : float = peso / (altura * altura)

print("SEU IMC E: ", imc)

if imc < 18.5 :
    print("Abaixo do Peso")
elif imc >= 18.6 and imc <= 24.9 :
    print("Peso Ideal")
elif imc >= 25.0 and imc <= 29.9 :
    print("Levemente Acima do Peso")    
elif imc >= 30.0 and imc <= 34.9 :
    print("Obesidade grau I")
elif imc >= 35.0 and imc <= 39.9 :
    print("Obsidade Grau II")
elif imc > 40 :
    print("Obsidade III")      


##///EXERCICIO 3
print("Insira Abaixo as Informações Referentes à Área")
print("")
larguraArea: float = float(input("Digite a Largura da Área: "))
comprimentoArea: float = float(input("Digite o Comprimento da Área: "))
print("Insira Abaixo as Informações Referentes ao Azulejo")
print("")
azulejoLargura: float = float(input("Insira a Largura do Azulejo: "))
azulejoComprimento: float = float(input("Insira o Comprimento do Azulejo: "))

# Calculando a área total e a área do azulejo
areaTotal: float = larguraArea * comprimentoArea
areaDoAzulejo: float = azulejoComprimento * azulejoLargura

# Calculando a quantidade de azulejos
quantidadeDeAzulejo: float = areaTotal / areaDoAzulejo

# Adicionando um excesso de 10% para cortes e bordas
excesso: float = 0.10
quantidadeAzulejosTotal = int(quantidadeDeAzulejo * (1 + excesso))

print(f"Quantidade de azulejos necessária (sem excesso): {int(quantidadeDeAzulejo)}")
print(f"Quantidade total de azulejos (com excesso): {quantidadeAzulejosTotal}")


##///EXERCICIO 4
n = int(input("Digite o número de Trechos: "))
distancias : list = []
tempos : list = []
velocidades : list= []

distanciaTotal = 0
tempoTotal = 0

for i in range(n):
    print(f"Trecho {i+1}:")
    distancia = float(input("  Digite a distância (km): "))
    tempo = float(input("  Digite o Tempo (h): "))

    distancias.append(distancia)
    tempos.append(tempo)

    velocidade = distancia / tempo
    velocidades.append(velocidade)

    distanciaTotal += distancia
    tempoTotal += tempo

    print(f"  Velocidade média no trecho {i+1}: {velocidade:.2f} Km/h")

# Fora do loop, após coletar todas as distâncias e tempos
velocidadeMediaTotal = distanciaTotal / tempoTotal
print(f"\nVelocidade média total: {velocidadeMediaTotal:.2f} km/h")

for i in range(n-1):
    aceleracao = (velocidades[i+1] - velocidades[i]) / tempos[i+1]
    print(f"Aceleração entre o trecho {i+1} e {i+2}: {aceleracao:.2f} km/h²")

###EXERCICIO 8
alunosQtd = int(input("Entre com a quantidade de alunos: "))

notasAll = []
somaNotas : float = 0

for i in range(alunosQtd):
    nota = float(input("Entre com a nota do aluno {}: ".format(i + 1)))
    notasAll.append(nota)

for nota in notasAll:
    somaNotas += nota

media : float = somaNotas / alunosQtd    

print("Notas: ", notasAll)
print("Soma das notas: ", somaNotas)
print("Média das notas: ", media)

