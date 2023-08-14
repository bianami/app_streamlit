import streamlit as st

# Defina as perguntas e respostas
questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Paris", "Londres", "Berlim"],
        "correct_answer": "Paris"
    },
    {
        "question": "Qual é o maior planeta do sistema solar?",
        "options": ["Terra", "Júpiter", "Marte"],
        "correct_answer": "Júpiter"
    },
    {
        "question": "Qual é a cor do céu em um dia claro?",
        "options": ["Verde", "Azul", "Vermelho"],
        "correct_answer": "Azul"
    }
]

def main():
    st.title("Jogo de Perguntas e Respostas")
    total_questions = len(questions)
    score = 0
    
    for i, q in enumerate(questions):
        st.write(f"**Pergunta {i+1}:** {q['question']}")
        answer = st.radio("Escolha a resposta:", q['options'])
        if answer == q['correct_answer']:
            score += 1
            st.write("Resposta correta!")
        else:
            st.write("Resposta incorreta.")
        
        if i < total_questions - 1:
            st.button("Próxima Pergunta")
    
    st.write(f"Seu placar final: {score}/{total_questions}")

if __name__ == "__main__":
    main()
