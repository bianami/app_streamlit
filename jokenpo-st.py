import streamlit as st
import random

def main():
    st.title("Jogo de Pedra, Papel e Tesoura")

    user_choice = st.radio("Escolha sua jogada:", ["pedra", "papel", "tesoura"])
    st.write(f"Você escolheu: {user_choice}")
    
    # Gera uma escolha aleatória para o computador
    computer_choice = random.choice(options)
    st.write(f"Computador escolheu: {computer_choice}")
    
    # Determina o resultado do jogo
    result = determine_winner(user_choice, computer_choice)

    st.title("Animação de Texto no Streamlit")
    
    st.write(resultado)
    
    # Use HTML para criar a animação de texto
    st.markdown(
        <div class="animation">
            <h2>Texto Animado</h2>
        </div>
        <style>
            .animation h2 {
                animation: slideIn 3s ease infinite;
            }
            
            @keyframes slideIn {
                0% {
                    transform: translateX(-100%);
                    opacity: 0;
                }
                100% {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        </style>
    )

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
