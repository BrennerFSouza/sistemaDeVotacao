candidatos = [
    ["Ana", "Carlos", "Beatriz", "João"],
    [0,0,0,0]
]
nulo = 0
branco = 0
totalVotos = 0
seletorCandidato = -1

def exibeCandidatos(candidatos):
    print("Lista de Candidatos:\n")
    for i in range(4):
        print(f"  {i+1} - {candidatos[0][i]}")

    print(" ------------------------------")
    print("  5 - Voto Nulo \n  6 - Voto em Branco\n  0 - Finalizar Votação\n")
    print(f"VOTOS REGISTRADOS: {totalVotos}")

def exibeTotalDeVotos(candidatos):
    print("\nTotal de Votos por Candidatos\n")
    for i in range(4):
        print(f" {candidatos[0][i]} - {candidatos[1][i]}")
    print(" -----------------------------")
    print(f"  Nulos - {nulo}")
    print(f"  Brancos - {branco}")

    print(f"\n VOTOS CONTABILIZADOS: {totalVotos}")

def exibePorcentagemDeVotos(candidatos):
    print("\nPorcentagem de Votos\n")

    if  totalVotos == 0:
        print("Porcentagem de Votos Nulos: 0%")
        print("Porcentagem de Votos em Branco: 0%")
        return

    print(f"Porcentagem de Votos Nulos: {nulo / totalVotos:.2%}")
    print(f"Porcentagem de Votos em Branco: {branco / totalVotos:.2%}")


def exibeVencedor(candidatos):

    if totalVotos - (nulo + branco) == 0:
        print("\n!!!Não houve vencedor!!!\n    Nenhum candidato obteve votos")
        return

    maiorQuantidadeDeVotos = 0
    candidatosComQuantidadeIgualDeVotos = 0


    for i in range(4):
        if candidatos[1][i] > maiorQuantidadeDeVotos:
            maiorQuantidadeDeVotos = candidatos[1][i]
            candidatosComQuantidadeIgualDeVotos = 1

        elif candidatos[1][i] == maiorQuantidadeDeVotos:
            candidatosComQuantidadeIgualDeVotos += 1

    if candidatosComQuantidadeIgualDeVotos == 1:
        print("\n!!!Vencedor!!!\n")
        for i in range(4):
            if candidatos[1][i] == maiorQuantidadeDeVotos:
                print(candidatos[0][i])
                print(f"  Quantidade de Votos:  {candidatos[1][i]}")
                print(f"\n  Tiveram {maiorQuantidadeDeVotos / totalVotos: .2%} votos")
                break

    else:
        print("\n!!!Empate!!!\n")
        for i in range(4):
            if candidatos[1][i] == maiorQuantidadeDeVotos:
                print(f"  {candidatos[0][i]}")
        print(f"\n  Tiveram {maiorQuantidadeDeVotos} votos")
        print(f"\n  Tiveram {maiorQuantidadeDeVotos / totalVotos: .2%} votos")

print("!!! Sistema de Votação !!!\n")

while seletorCandidato != 0:

    exibeCandidatos(candidatos)
    seletorCandidato = int(input("Digite o número do seu candidato: "))

    if seletorCandidato == 0:
        print("Votação finalizada!\n\n")
        break

    if 1 <= seletorCandidato <= 6:
        totalVotos += 1

        if 1 <= seletorCandidato <= 4:
            candidatos[1][seletorCandidato - 1] += 1
        elif seletorCandidato == 5:
            nulo += 1
        elif seletorCandidato == 6:
            branco += 1


    else:
        print("!!!Valor Inválido!!!")


exibeTotalDeVotos(candidatos)
exibePorcentagemDeVotos(candidatos)
exibeVencedor(candidatos)