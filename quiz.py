import streamlit as st

# Função para a página 1
def page1():
    st.title("Página 1 - Pergunta 1")
    st.write("Qual é a capital da França?")
    options = ["Paris", "Londres", "Berlim"]
    answer = st.radio("Escolha a resposta:", options)
    return answer

# Função para a página 2
def page2():
    st.title("Página 2 - Pergunta 2")
    st.write("Qual é o maior planeta do sistema solar?")
    options = ["Terra", "Júpiter", "Marte"]
    answer = st.radio("Escolha a resposta:", options)
    return answer

# Função para a página 3
def page3():
    st.title("Página 3 - Pergunta 3")
    st.write("Qual é a cor do céu em um dia claro?")
    options = ["Verde", "Azul", "Vermelho"]
    answer = st.radio("Escolha a resposta:", options)
    return answer

# Função principal
def main():
    st.sidebar.title("Navegação")
    page_options = ["Página 1", "Página 2", "Página 3"]
    selected_page = st.sidebar.radio("Selecione a página:", page_options)
    
    if selected_page == "Página 1":
        answer1 = page1()
        st.sidebar.write("Resposta Pergunta 1:", answer1)
    elif selected_page == "Página 2":
        answer2 = page2()
        st.sidebar.write("Resposta Pergunta 2:", answer2)
    elif selected_page == "Página 3":
        answer3 = page3()
        st.sidebar.write("Resposta Pergunta 3:", answer3)
    
    if st.sidebar.button("Mostrar Resultado"):
        st.write("Resultado Final:")
        st.write("Resposta Pergunta 1:", answer1)
        st.write("Resposta Pergunta 2:", answer2)
        st.write("Resposta Pergunta 3:", answer3)

if __name__ == "__main__":
    main()
