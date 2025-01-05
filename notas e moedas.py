"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal."""

def conversao(n):
    notas = {"cem" : 0,
        "cinquenta" : 0,
        "vinte" : 0,
        "dez" : 0,
        "cinco" : 0,
            "dois" : 0}

    moedas = {"um" : 0,
            "cinquenta" : 0,
            "vinteCinco" : 0,
            "dez" : 0,
            "cinco" : 0,
            "umcen" : 0}

    dinheiro_em_centavos = round(dinheiro * 100)

    if dinheiro_em_centavos >= 10000:
        notas['cem'] = dinheiro_em_centavos // 10000
        dinheiro_em_centavos %= 10000

    if dinheiro_em_centavos >= 5000:
        notas['cinquenta'] = dinheiro_em_centavos // 5000
        dinheiro_em_centavos %= 5000

    if dinheiro_em_centavos >= 2000:
        notas['vinte'] = dinheiro_em_centavos // 2000
        dinheiro_em_centavos %= 2000

    if dinheiro_em_centavos >= 1000:
        notas['dez'] = dinheiro_em_centavos // 1000
        dinheiro_em_centavos %= 1000

    if dinheiro_em_centavos >= 500:
        notas['cinco'] = dinheiro_em_centavos // 500
        dinheiro_em_centavos %= 500

    if dinheiro_em_centavos >= 200:
        notas['dois'] = dinheiro_em_centavos // 200
        dinheiro_em_centavos %= 200

    if dinheiro_em_centavos >= 100:
        moedas['um'] = dinheiro_em_centavos // 100
        dinheiro_em_centavos %= 100

    if dinheiro_em_centavos >= 50:
        moedas['cinquenta'] = dinheiro_em_centavos // 50
        dinheiro_em_centavos %= 50

    if dinheiro_em_centavos >= 25:
        moedas['vinteCinco'] = dinheiro_em_centavos // 25
        dinheiro_em_centavos %= 25

    if dinheiro_em_centavos >= 10:
        moedas['dez'] = dinheiro_em_centavos // 10
        dinheiro_em_centavos %= 10

    if dinheiro_em_centavos >= 5:
        moedas['cinco'] = dinheiro_em_centavos // 5
        dinheiro_em_centavos %= 5

    if dinheiro_em_centavos >= 1:
        moedas['umcen'] = dinheiro_em_centavos // 1
        dinheiro_em_centavos %= 1


    print("NOTAS:")
    print(f"{notas['cem']} nota(s) de R$ 100.00")
    print(f"{notas['cinquenta']} nota(s) de R$ 50.00")
    print(f"{notas['vinte']} nota(s) de R$ 20.00")
    print(f"{notas['dez']} nota(s) de R$ 10.00")
    print(f"{notas['cinco']} nota(s) de R$ 5.00")
    print(f"{notas['dois']} notas(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{moedas['um']} moeda(s) de R$ 1.00")
    print(f"{moedas['cinquenta']} moeda(s) de R$ 0.50")
    print(f"{moedas['vinteCinco']} moeda(s) de R$ 0.25")
    print(f"{moedas['dez']} moeda(s) de R$ 0.10")
    print(f"{moedas['cinco']} moeda(s) de R$ 0.05")
    print(f"{moedas['umcen']} moeda(s) de R$ 0.01")


dinheiro = float(input("Digite a quantia de dinheiro que sera convertido: "))
conversao(dinheiro)
