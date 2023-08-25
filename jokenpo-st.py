# importação das bibliotecas necessárias
import streamlit as st
import random


def main():
    
    st.title("Jogo de Jokenpô")
    
    options = ["pedra", "papel", "tesoura"]
    
    user_choice = st.radio("Escolha sua jogada:", options)
    st.write(f"Você escolheu: {user_choice}")
    
    # Gera uma escolha aleatória para o computador
    computer_choice = random.choice(options)
    st.write(f"Computador escolheu: {computer_choice}")
    
    # Determina o resultado do jogo
    result = determine_winner(user_choice, computer_choice)

    if "perdeu" in result.lower():
            #st.write("VoCê perdeu")    
        st.markdown("<p style='color:red; text-align: center; font-size:18px;'{result}", unsafe_allow_html=True)
    if "ganhou" in result.lower():
            st.balloons()
            st.write(result, text_align='center')
    else:
            st.write(result, text_align='center')
        

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
         (user_choice == "papel" and computer_choice == "pedra") or \
         (user_choice == "tesoura" and computer_choice == "papel"):
        return "Você ganhou!"
    else:
        return "Você perdeu"
    
if __name__ == "__main__":
    main()
