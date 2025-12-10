import os
import time

# --- 1. Estrutura de Dados ---

class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# Vetores globais (4 posições)
lista_avioes = [None] * 4
lista_assentos = [0] * 4
lista_reservas = [] # Armazena os objetos da classe Reserva
MAX_RESERVAS = 10

# --- 2. Funções do Sistema ---

def registrar_avioes():
    print("\n--- Registro de Aviões ---")
    for i in range(4):
        lista_avioes[i] = input(f"Digite o número/identificação do avião {i+1}: ")
    print("\nAviões registrados com sucesso!")

def registrar_assentos():
    print("\n--- Registro de Assentos ---")
    # Verifica se os aviões já foram cadastrados (se o primeiro não é None)
    if lista_avioes[0] is None:
        print("\nErro: É necessário cadastrar os aviões (Opção 1) primeiro.")
        return

    for i in range(4):
        while True:
            try:
                qtd = int(input(f"Quantos assentos para o avião {lista_avioes[i]}? "))
                if qtd >= 0:
                    lista_assentos[i] = qtd
                    break
                else:
                    print("A quantidade não pode ser negativa.")
            except ValueError:
                print("Por favor, digite um número inteiro.")
    print("\nQuantidade de assentos atualizada!")

def reservar_passagem():
    print("\n--- Nova Reserva ---")
    
    if len(lista_reservas) >= MAX_RESERVAS:
        print("\nLimite máximo de 10 reservas atingido!")
        return

    if lista_avioes[0] is None:
        print("\nErro: Nenhum avião cadastrado.")
        return

    aviao_solicitado = input("Informe o número do avião: ")

    # Verifica se avião existe
    if aviao_solicitado not in lista_avioes:
        print("\nEste avião não existe!")
    else:
        # Pega o índice do avião para checar os assentos correspondentes
        indice = lista_avioes.index(aviao_solicitado)

        if lista_assentos[indice] > 0:
            nome = input("Informe o nome do passageiro: ")
            
            # Atualiza dados
            lista_assentos[indice] -= 1
            nova_reserva = Reserva(aviao_solicitado, nome)
            lista_reservas.append(nova_reserva)
            
            print("\nReserva realizada com sucesso!")
        else:
            print("\nNão há assentos disponíveis para este avião!")

def consultar_por_aviao():
    print("\n--- Consulta por Avião ---")
    aviao_busca = input("Informe o número do avião: ")

    if aviao_busca not in lista_avioes:
        print("\nEste avião não existe!")
        return

    encontrou = False
    print(f"\nReservas para o avião {aviao_busca}:")
    for reserva in lista_reservas:
        if reserva.numero_aviao == aviao_busca:
            print(f"- Passageiro: {reserva.nome_passageiro}")
            encontrou = True
    
    if not encontrou:
        print("Não há reservas realizadas para este avião!")

def consultar_por_passageiro():
    print("\n--- Consulta por Passageiro ---")
    nome_busca = input("Informe o nome do passageiro: ")

    encontrou = False
    print(f"\nVoos de {nome_busca}:")
    for reserva in lista_reservas:
        if reserva.nome_passageiro.lower() == nome_busca.lower():
            print(f"- Avião: {reserva.numero_aviao}")
            encontrou = True
            
    if not encontrou:
        print("Não há reservas realizadas para este passageiro!")

# --- 3. Menu Principal (Seguindo seu modelo) ---

while True:
    print("""
          --- Sistema Sweet Flight ---
          1 - Registrar Aviões
          2 - Registrar Assentos
          3 - Reservar Passagem
          4 - Consultar por Avião
          5 - Consultar por Passageiro
          6 - sair
          """)
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            registrar_avioes()
        case 2:
            registrar_assentos()
        case 3:
            reservar_passagem()
        case 4:
            consultar_por_aviao()
        case 5:
            consultar_por_passageiro()
        case 6:
            print("\nFechando o sistema Sweet Flight...")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")

    # Lógica de espera para leitura antes de limpar a tela (exceto ao sair)
    if opcao != 6:
        input("\nPressione Enter para continuar...") # Pausa para ler o resultado
        os.system("cls || clear")