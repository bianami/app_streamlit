
import streamlit as st
import random
from PIL import Image

def main():
    st.title("Jogo de Pedra, Papel e Tesoura")
    
    # Faz o upload das imagens
    rock_image = Image.open("rock.png")
    paper_image = Image.open("paper.png")
    scissors_image = Image.open("scissors.png")
    
    # Cria duas colunas para exibir as imagens lado a lado
    col1, col2, col3 = st.beta_columns(3)
    
    # Exibe as imagens nas colunas
    with col1:
        st.image(rock_image, caption="Pedra", width=100)
    with col2:
        st.image(paper_image, caption="Papel", width=100)
    with col3:
        st.image(scissors_image, caption="Tesoura", width=100)
    
    # Gera uma escolha aleatória para o computador
    computer_choice = random.choice(["Pedra", "Papel", "Tesoura"])
    
    # Exibe o resultado do jogo
    result = play_game(computer_choice)
    st.write(result)

def play_game(computer_choice):
    user_choice = None
    
    # Espera até que o usuário faça uma escolha
    with st.form("Escolha sua jogada"):
        with st.beta_container():
            user_choice = st.selectbox("Escolha sua jogada:", ["Pedra", "Papel", "Tesoura"])
            st.write(f"Você escolheu: {user_choice}")
            
            # Botão para submeter a escolha
            submit_button = st.form_submit_button(label="Jogar")
    
    if user_choice:
        # Determina o resultado do jogo
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
