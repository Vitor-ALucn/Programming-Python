import random
import os

# Configuração da fila
TAMANHO_FILA = 25
fila = [0] * TAMANHO_FILA
cont_vetor = 1  # Começa na posição 1 (como no VisualG)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def enqueue():
    global cont_vetor
    if cont_vetor <= TAMANHO_FILA:
        valor = random.randint(1, 100)  # Gera número aleatório
        fila[cont_vetor - 1] = valor
        print(f"Número {valor} adicionado à fila.")
        cont_vetor += 1
    else:
        print("Erro: Fila cheia! Não é possível adicionar.")
    input("Pressione Enter para continuar...")

def dequeue():
    global cont_vetor
    if cont_vetor > 1:
        for i in range(cont_vetor - 1):
            fila[i] = fila[i + 1]
        fila[cont_vetor - 1] = 0
        cont_vetor -= 1
        print("O primeiro elemento foi removido da fila!")
    else:
        print("Erro: Fila vazia! Não há elementos para remover.")
    input("Pressione Enter para continuar...")

def clean():
    global cont_vetor
    for i in range(TAMANHO_FILA):
        fila[i] = 0
    cont_vetor = 1
    print("Fila limpa com sucesso!")
    input("Pressione Enter para continuar...")

def view():
    limpar_tela()
    print("Conteúdo da fila:")
    if cont_vetor == 1:
        print("Fila vazia.")
    else:
        for i in range(cont_vetor - 1):
            print(f"[{i + 1}] = {fila[i]}")
    input("Pressione Enter para continuar...")

# Menu principal
while True:
    limpar_tela()
    print("---------------------------------------")
    print("A) ADICIONAR (adiciona elemento no fim da fila)")
    print("B) REMOVER (remove o elemento do início da fila)")
    print("C) LIMPAR (remove todos os elementos)")
    print("D) LISTAR (lista todos os elementos)")
    print("---------------------------------------")
    opcao = input("Escolha uma das opções: ").upper()

    if opcao == "A":
        enqueue()
    elif opcao == "B":
        dequeue()
    elif opcao == "C":
        clean()
    elif opcao == "D":
        view()
    else:
        print("Opção inválida! Saindo...")
        break