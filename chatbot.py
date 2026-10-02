# ==================================================
# 🤖 MEU PRIMEIRO CHATBOT
# ==================================================

# Importa a ferramenta random
# Ela permite escolher respostas aleatórias.
import random


# --------------------------------------------------
# APRESENTAÇÃO
# --------------------------------------------------

# Mostra uma mensagem na tela.
print("===================================")
print("🤖 MEU PRIMEIRO CHATBOT")
print("===================================")

# Pergunta o nome do usuário.
nome = input("🤖 Qual é o seu nome? ")

# Cumprimenta o usuário.
print("🤖 Prazer em conhecer você, " + nome + "!")

# Explica como sair.
print("🤖 Digite 'sair' quando quiser terminar a conversa.")
print()


# --------------------------------------------------
# LISTAS DE RESPOSTAS
# --------------------------------------------------

# Lista de respostas para quando o usuário disser "oi".
respostas_oi = [
    "Olá! 😄",
    "Oi! Tudo bem?",
    "E aí! Que legal falar com você!",
    "Olá! Como está seu dia?"
]


# Lista de respostas para quando o usuário
# perguntar como o chatbot está.
respostas_como_estou = [
    "Estou muito bem! 😄",
    "Estou ótimo!",
    "Tudo tranquilo por aqui!",
    "Estou pronto para conversar! 🤖"
]


# --------------------------------------------------
# LOOP DE CONVERSA
# --------------------------------------------------

# O while faz o chatbot continuar conversando.
while True:

    # Pede uma nova mensagem para o usuário.
    mensagem = input("🧑 Você: ")

    # Transformamos a mensagem em letras minúsculas.
    # Assim "OI", "Oi" e "oi" podem ser tratados
    # da mesma maneira.
    mensagem = mensagem.lower()

    # --------------------------------------------------
    # SAIR
    # --------------------------------------------------

    # Verifica se o usuário quer sair.
    if mensagem == "sair":

        # Mensagem de despedida.
        print("🤖 Até mais, " + nome + "! 👋")

        # Encerra o loop.
        break


    # --------------------------------------------------
    # SAUDAÇÃO
    # --------------------------------------------------

    elif mensagem == "oi":

        # Escolhe uma resposta aleatória.
        resposta = random.choice(respostas_oi)

        # Mostra a resposta.
        print("🤖 " + resposta)


    # --------------------------------------------------
    # COMO O BOT ESTÁ?
    # --------------------------------------------------

    elif mensagem == "como você está":

        # Escolhe uma resposta aleatória.
        resposta = random.choice(respostas_como_estou)

        # Mostra a resposta.
        print("🤖 " + resposta)


    # --------------------------------------------------
    # PERGUNTA SOBRE O NOME DO BOT
    # --------------------------------------------------

    elif mensagem == "qual é seu nome":

        print("🤖 Eu sou o ChatBot Junior!")

    # --------------------------------------------------
    # IDADE
    # --------------------------------------------------

    elif mensagem == "qual seu filme favorito":

        print(" Eu tenho 1 dia de idade... porque fui criado hoje! 😂")

    elif mensagem == "como você está":

        # Escolhe uma resposta aleatória.

        # Mostra a resposta.
        print("🤖 " + resposta)


    # --------------------------------	------------------
    # AGRADECIMENTO
    # --------------------------------------------------

    elif mensagem == "obrigado" or mensagem == "obrigada":

        print("🤖 De nada! 😊")


    # --------------------------------------------------
    # QUALQUER OUTRA MENSAGEM
    # --------------------------------------------------

    else:

        # Resposta padrão quando o bot não conhece
        # a mensagem.
        print("🤖 Hmm... ainda estou aprendendo!")
        print("🤖 Você pode tentar falar 'oi' ou 'como você está'.")


# --------------------------------------------------
# FIM DO PROGRAMA
# --------------------------------------------------

print("🤖 Programa encerrado.")
