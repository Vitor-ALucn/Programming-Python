# Definindo as plantas
flower = 'Spathiphyllum'
flower2 = 'pelargonium'
flower3 = 'spathiphyllum'

# Pergunta ao usuário e armazena a resposta
resposta = input("Qual a planta que no seu interior filtra as toxinas nocivas do ar? ")

# Verifica a resposta do usuário
if resposta == flower:
    print('Spathiphyllum! Aliás, é a melhor planta filtrante de todos os tempos!')

elif resposta == flower2:
    print("Você quis dizer Spathiphyllum!? Não pelargonium, certo?")

elif resposta == flower3:
    print("Você escreveu spathiphyllum, mas é com 'S' maiúsculo: Spathiphyllum!")

else:
    print("Não, a planta mágica é Spathiphyllum! 🌿")