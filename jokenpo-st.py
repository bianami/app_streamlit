import streamlit as st
import random

def main():
    st.title("Jogo de Pedra, Papel e Tesoura")
    
    user_choice = None
    
    st.write("Escolha uma opção:")
    
    # Criação dos botões
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button("Pedra"):
            user_choice = "pedra"
    with col2:
        if st.button("Papel"):
            user_choice = "papel"
    with col3:
        if st.button("Tesoura"):
            user_choice = "tesoura"
    
    if user_choice:
        computer_choice = random.choice(["pedra", "papel", "tesoura"])
        result = determine_winner(user_choice, computer_choice)
        st.write(f"Você escolheu: {user_choice.capitalize()}")
        st.write(f"Computador escolheu: {computer_choice.capitalize()}")
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
Neste exemplo, usamos a função st.button() para criar os botões "Pedra", "Papel" e "Tesoura". Quando o usuário clica em um dos botões, a escolha do usuário é registrada, e então o computador faz sua escolha aleatória. Em seguida, o resultado do jogo é determinado usando a função determine_winner().

Lembre-se de que você pode estilizar e personalizar ainda mais o layout e a aparência dos botões, se desejar.





