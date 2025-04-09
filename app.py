import streamlit as st
import time

st.set_page_config(page_title="Quiz de 5 meses de casados", page_icon="💖")
st.image("foto.jpg", use_column_width=True)
st.title("Quiz de 5 meses de casados 💍")
st.markdown("### Gabriela & Pedro")
st.write("Bem-vindo ao nosso quiz especial de 5 meses de casamento! 💑")
st.write("Responda com amor, porque a surpresa no final é feita com carinho 💌")
st.write("---")

perguntas = [
    {
        "pergunta": "Onde foi nosso primeiro beijo?",
        "opcoes": ["Violeta", "CSN", "Restaurante Japonês", "Sua casa"],
        "resposta": "Violeta"
    },
    {
        "pergunta": "O que eu mais amo em você?",
        "opcoes": ["Inteligência", "Aparência", "Cheirinho bom", "Virilidade"],
        "resposta": "Cheirinho bom"
    },
    {
        "pergunta": "Onde foi o nosso date em que rolou o primeiro 'eu te amo'?",
        "opcoes": ["Cinema", "Japonês", "Lanchonete de hot dog", "Praia"],
        "resposta": "Praia"
    },
    {
        "pergunta": "O que mais amo fazer nas sextas feiras?",
        "opcoes": [
            "Date semanal com comidinha, filme/anime e chamego",
            "Barzinho com os amigos",
            "Dormir e descansar",
            "Fazer vários nadas"
        ],
        "resposta": "Date semanal com comidinha, filme/anime e chamego"
    },
    {
        "pergunta": "Quem ama mais?",
        "opcoes": ["Pedro", "Romeiro", "Vido", "A Gabi, é óbvio"],
        "resposta": "A Gabi, é óbvio"
    }
]

respostas = []
for i, p in enumerate(perguntas):
    st.subheader(f"{i+1}. {p['pergunta']}")
    resposta = st.radio("Escolha uma opção:", p['opcoes'], key=i)
    respostas.append((resposta, p['resposta']))
    st.write("---")

if st.button("Enviar respostas 💘"):
    acertos = sum([1 for r in respostas if r[0] == r[1]])
    st.success("Respostas enviadas!")
    st.balloons()
    time.sleep(1)

    st.header("Resultado 🎉")
    if acertos == len(perguntas):
        st.write("Você acertou tudo! Perfeição tem nome: Pedro 💖")
    else:
        st.write(f"Você acertou {acertos}/{len(perguntas)}... mas já ganhou meu coração faz tempo 😘")

    time.sleep(1.5)
    st.subheader("Agora... uma surpresinha 🎶")

    st.write("Clique abaixo para ouvir a nossa música:")
    st.link_button("🎧 Ouvir 'I Wanna Be Yours' no Spotify", "https://open.spotify.com/track/4Yd7RZDO5mZBlalS2mVQFg")

    st.write("---")
    st.markdown("""
#### 💌 Mensagem final da Gabi:
Sou muito mais feliz quando estamos juntos e quando vivemos nossos propósitos. 

Espero te fazer feliz por muitos anos e que encontre em mim o que tem de extra em você. 

Que eu te transborde assim como você me transborda.  

Eu amo muito você, mais do que é possível imaginar. Obrigada por me permitir viver até aqui com você, estou pronta e ansiando por mais. 💖
""")
