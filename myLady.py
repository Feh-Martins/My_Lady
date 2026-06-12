import streamlit as st
import base64
import time
from datetime import datetime
from zoneinfo import ZoneInfo


# ==========================
# FUNÇÕES DO FUNDO
# ==========================

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)

    page_bg_img = f"""
    <style>

    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.45),
                rgba(0,0,0,0.45)
            ),
            url("data:image/jpeg;base64,{bin_str}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main .block-container {{
        max-width: 850px;
    }}

    h1, h2, h3, h4, h5, h6,
    p,
    label,
    span,
    li,
    div[data-testid="stMarkdownContainer"] {{
        color: white !important;
    }}

    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)


# Define o fundo
set_bg_hack("foto.jpg")


# ==========================
# CONTEÚDO
# ==========================

st.title("❤️ Para meu amor, minha Lady")
st.write("---")

tz = ZoneInfo("America/Sao_Paulo")

data_inicio = datetime(
    2025,
    9,
    15,
    0,
    0,
    0,
    tzinfo=tz,
)

agora = datetime.now(tz)

dias = (agora - data_inicio).days
horas = agora.hour
minutos = agora.minute
segundos = agora.second

st.markdown(
    f"""
### Já estamos juntos há:

# {dias} dias, {horas}h, {minutos}m e {segundos}s que iniciamos nosso amor.
"""
)

st.markdown(
    """
### Você deixa tudo mais bonito

Às vezes, a vida nos presenteia de maneira que não entendemos.

Cada detalhe, cada momento compartilhado com você é uma melodia suave.
"""
)

# ==========================
# BOTÃO
# ==========================

if "clicado" not in st.session_state:
    st.session_state.clicado = False

if st.button("Clique aqui ❤️"):
    st.session_state.clicado = True

if st.session_state.clicado:

    st.markdown(
        "<h1 style='text-align:center;'>❤️ ❤️ ❤️</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.video("0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4")

    st.success("Minha Amada Princesa!")
    st.success("Para sempre vou te amar.")
    st.success("Obrigado por ser a trilha sonora perfeita da minha vida. ❤️")


# ==========================
# ATUALIZAÇÃO DO CONTADOR
# ==========================

time.sleep(1)
st.rerun()
