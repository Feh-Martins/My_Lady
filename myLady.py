import streamlit as st
import base64
import time
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="Para meu amor ❤️",
    page_icon="❤️",
    layout="centered",
)


# ============================================
# FUNÇÕES
# ============================================

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


def set_bg(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)

    st.markdown(
        f"""
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

        section[data-testid="stMain"] {{
            background: transparent;
        }}

        h1,h2,h3,h4,h5,h6,p,span,label {{
            color: white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


set_bg("foto.jpg")


# ============================================
# TÍTULO
# ============================================

st.title("❤️ Para meu amor, minha Lady")
st.divider()


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


# ============================================
# CONTADOR
# ============================================

@st.fragment(run_every="1s")
def contador():

    agora = datetime.now(tz)
    diferenca = agora - data_inicio

    dias = diferenca.days

    horas_totais = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60
    segundos = diferenca.seconds % 60

    st.markdown(
        f"""
### Iniciamos nosso amor e já estamos juntos há

# {dias} dias, {horas_totais}h, {minutos}m e {segundos}s
"""
    )


contador()


# ============================================
# TEXTO
# ============================================

st.markdown(
    """
### Você deixa tudo mais bonito

Às vezes, a vida nos presenteia de maneira que não entendemos.

Cada detalhe, cada momento compartilhado com você é uma melodia suave.
"""
)


# ============================================
# BOTÃO
# ============================================

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
        st.video(
            "0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4"
        )

    st.success("Minha Amada Princesa!")
    st.success("Para sempre vou te amar.")
    st.success(
        "Obrigado por ser a trilha sonora perfeita da minha vida. ❤️"
    )
