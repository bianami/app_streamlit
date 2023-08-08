import streamlit as st
import random
from PIL import Image


def main():
    st.title("Jogo de Pedra, Papel e Tesoura")

    # Faz o upload das imagens
    rock_image = Image.open("rock.png")
    paper_image = Image.open("paper.png")
    scissors_image = Image.open("scissors.png")

    # Exibe as imagens para que o usuário possa clicar nelas
    user_choice = st.image([rock_image, paper_image, scissors_image], caption=["Pedra", "Papel", "Tesoura"], width=150)

    if user_choice:
        user_choice = user_choice[0]
        st.write(f"Você escolheu: {user_choice.caption}")

        # Gera uma escolha aleatória para o computador
        computer_choice = random.choice(["Pedra", "Papel", "Tesoura"])
        st.write(f"Computador escolheu: {computer_choice}")

        # Determina o resultado do jogo
        result = determine_winner(user_choice.caption, computer_choice)
        st.write(result)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "Pedra" and computer_choice == "Tesoura") or \
            (user_choice == "Papel" and computer_choice == "Pedra") or \
            (user_choice == "Tesoura" and computer_choice == "Papel"):
        return "Você ganhou!"
    else:
        return "Você perdeu!"


if __name__ == "__main__":
    main()