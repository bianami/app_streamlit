import streamlit as st

st.title("Jogo de Perguntas!")

questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Londres", "Paris", "Madri", "Berlim"],
        "correct_index": 1
    },
    {
        "question": "Qual é o maior planeta do sistema solar?",
        "options": ["Terra", "Júpiter", "Marte", "Vênus"],
        "correct_index": 1
    },
    {
        "question": "Quantas cores tem um arco-íris?",
        "options": ["5", "7", "3", "6"],
        "correct_index": 1
    }
]

total_questions = len(questions)
score = 0
current_question = 0

if current_question < total_questions:
    st.write(f"**Pergunta {current_question + 1}/{total_questions}:** {questions[current_question]['question']}")
    selected_option = st.radio("Escolha a sua resposta:", questions[current_question]["options"])
    
    if st.button("Próxima Pergunta"):
        if selected_option == questions[current_question]["options"][questions[current_question]["correct_index"]]:
            score += 1
        current_question += 1

if current_question >= total_questions:
    st.write(f"Você acertou {score} de {total_questions} perguntas!")
