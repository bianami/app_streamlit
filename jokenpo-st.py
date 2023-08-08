import streamlit as st
import random

def main():
    st.title("Jogo de Pedra, Papel e Tesoura")

    options = ["pedra", "papel", "tesoura"]
    
    user_choice = st.radio("Escolha sua jogada:", options)
    st.write(f"Você escolheu: {user_choice}")
    
    # Gera uma escolha aleatória para o computador
    computer_choice = random.choice(options)
    st.write(f"Computador escolheu: {computer_choice}")
    
    # Determina o resultado do jogo
    result = determine_winner(user_choice, computer_choice)

     if "perdeu" in result.lower():
            st.markdown("<p style='color:red; font-size:20px;'>Você perdeu!</p>", unsafe_allow_html=True)
    if "ganhou" in result.lower():
            st.balloons()
            st.write(result)
    else:
            st.write(result)
        
    


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
         (user_choice == "papel" and computer_choice == "pedra") or \
         (user_choice == "tesoura" and computer_choice == "papel"):
        return "Você ganhou!"
    else:
        return "Você perdeu!"
    
if __name__ == "__main__":
    main()
