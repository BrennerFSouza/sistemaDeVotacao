# Variáveis

candidatos = [
    ["Ana", "Carlos", "Beatriz", "João"],
    [0,0,0,0]
] #armazenar candidatos e contagem de votos
nulo = 0    # Contagem de votos nulos
branco = 0  # Contagem de votos em branco
totalVotos = 0  # Total de votos contabilizados
seletorCandidato = -1  # Variável para armazenar a escolha do usuário


#Funções

## Exibe a tabela de candidatos no console
def exibeCandidatos():
    print("Lista de Candidatos:\n")
        #Loop que percorre a Matriz candidatos e os exibe
    for i in range(4):
        print(f"  {i+1} - {candidatos[0][i]}")

    print(" ------------------------------")
    print("  5 - Voto Nulo \n  6 - Voto em Branco\n  0 - Finalizar Votação\n")
    print(f"VOTOS REGISTRADOS: {totalVotos}")

##Exibe o total de votos dos candidatos, de votos em branco e votos nulos
def exibeTotalDeVotos():
    print("\nTotal de Votos por Candidatos\n")
    # Loop que percorre a Matriz candidatos e os exibe junto com sua quantidade de votos
    for i in range(4):
        print(f" {candidatos[0][i]} - {candidatos[1][i]}")
    print(" -----------------------------")
    print(f" Nulos - {nulo}")
    print(f" Brancos - {branco}")

    print(f"\n VOTOS CONTABILIZADOS: {totalVotos}")

## Exibe porcentagem de votos nulos e brancos em relação ao total de votos
def exibePorcentagemDeVotos():
    print("\nPorcentagem de Votos\n")

    if  totalVotos == 0:    # Evita divisão por zero caso não haja votos
        print("Porcentagem de Votos Nulos: 0%")
        print("Porcentagem de Votos em Branco: 0%")
        return

    print(f"Porcentagem de Votos Nulos: {nulo / totalVotos:.2%}")
    print(f"Porcentagem de Votos em Branco: {branco / totalVotos:.2%}")

## Exibe o nome do candidato ganhador
def exibevencedor(maiorQuantidadeDeVotos):
    print("\n!!!Vencedor!!!\n")
        #Percorre a matriz buscando o nome do candidato vencedor
    for i in range(4):
        if candidatos[1][i] == maiorQuantidadeDeVotos:
            print("***************")
            print(f"      {candidatos[0][i]}")
            print("***************")
            print(f"  Quantidade de Votos: {candidatos[1][i]}")
            print(f"\n  Teve {maiorQuantidadeDeVotos / totalVotos: .2%} dos votos")
            break

## Exibe lista de candidatos que empataram em primeiro lugar com a mesma quantidade de votos
def exibeEmpate(maiorQuantidadeDeVotos):
    print("\n!!!Empate!!!\n")
        # Percorre a matriz buscando o nome dos candidatos que a maior quantidade de votos
    for i in range(4):
        if candidatos[1][i] == maiorQuantidadeDeVotos:
            print(f"  {candidatos[0][i]}")
    print(f"\n  Tiveram {maiorQuantidadeDeVotos} votos")
    print(f"\n  Tiveram {maiorQuantidadeDeVotos / totalVotos: .2%} votos")

## Calcula se a votação acabou em empate ou com um ganhador
def calcularVencedor():
    maiorQuantidadeDeVotos = 0              # Armazena maior quantidade de votos
    candidatosComQuantidadeIgualDeVotos = 0 # Armazena quantos usuários tiveram aquela quantidade de votos

    # Verifica o maior número de votos entre os candidatos
    for i in range(4):
        if candidatos[1][i] > maiorQuantidadeDeVotos:
            maiorQuantidadeDeVotos = candidatos[1][i]
            candidatosComQuantidadeIgualDeVotos = 1

        elif candidatos[1][i] == maiorQuantidadeDeVotos:
            candidatosComQuantidadeIgualDeVotos += 1
    # Determina se há um vencedor ou empate
    if candidatosComQuantidadeIgualDeVotos == 1:
        exibevencedor(maiorQuantidadeDeVotos)

    else:
        exibeEmpate(maiorQuantidadeDeVotos)

## Verifica se houve votos para definir um ganhador
def verificaVotos():

    if totalVotos - (nulo + branco) == 0:
        print("\n!!!Não houve vencedor!!!\n    Nenhum candidato obteve votos")
        return

    calcularVencedor()



# Código

print("!!! Sistema de Votação !!!\n")

# Loop principal do sistema de votação, que roda até que o usuário digite "0"
while seletorCandidato != 0:

    #Exibe o menu mostrando as opções para o usuário
    exibeCandidatos()

    # Solicita o voto e valida a entrada para garantir que seja um número válido
    try:
        seletorCandidato = int(input("Digite o número do seu candidato: "))
    except ValueError:
        print("\n''''''''''''''''''''''''''''''''''''\n         !!!Valor Inválido!!! \n    Por favor, insira um número.\n''''''''''''''''''''''''''''''''''''")
        continue

    #Finaliza o loop caso o usuário pressione "0"
    if seletorCandidato == 0:
        print("Votação finalizada!\n\n")
        break

    #Reinicia o loop caso a opção do usuário não seja válida
    if seletorCandidato < 1 or seletorCandidato > 6:
        print("\n''''''''''''''''''''''''''''''''''''''''''\n         !!!Valor Inválido!!! \n    Por favor, insira um valor válido.\n''''''''''''''''''''''''''''''''''''''''''")
        continue

    #Incrementa variavel com total de votos
    totalVotos += 1

    #Incrementa voto do usuário conforme  sua escolha
    if 1 <= seletorCandidato <= 4:
        candidatos[1][seletorCandidato - 1] += 1
    elif seletorCandidato == 5:
        nulo += 1
    elif seletorCandidato == 6:
        branco += 1

#Fim While

# Exibe o resumo da votação e determina o vencedor ou empate
exibeTotalDeVotos()         # Exibe total de votos de cada candidato, votos em branco e nulos
exibePorcentagemDeVotos()   # Exibe porcentagem de votos nulos e brancos
verificaVotos()             # Calcula e exibe o vencedor ou empate