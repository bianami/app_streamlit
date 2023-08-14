import streamlit as st

def main():
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

    for i, question_data in enumerate(questions):
        st.write(f"**Pergunta {i + 1}/{total_questions}:** {question_data['question']}")
        selected_option = st.radio("Escolha a sua resposta:", question_data["options"])
        
        if st.button("Próxima Pergunta"):
            print('ola')
            if selected_option == question_data["options"][question_data["correct_index"]]:
                score += 1

    st.write(f"Você acertou {score} de {total_questions} perguntas!")

if __name__ == "__main__":
    main()
