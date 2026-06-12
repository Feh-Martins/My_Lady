import streamlit as st
import base64
from datetime import date

# Configuração da página
st.set_page_config(page_title="Para você", page_icon="❤️")

# --- Função de Fundo ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
    }}
    .stApp::before {{
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.5); z-index: -1;
    }}
    .main > .block-container {{ text-align: left !important; max-width: 800px; }}
    h1, h2, h3, p, div {{ color: white !important; text-align: left !important; }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_bg_hack('foto.jpg') 


# --- Cálculo de Dias ---
def calcular_dias(data_inicial):
    hoje = date.today()
    delta = hoje - data_inicial
    return delta.days

data_inicio = date(2025, 9, 15)
dias_juntos = calcular_dias(data_inicio)


# --- Lógica do Botão ---
# Inicializa o estado do botão se ele ainda não existir
if 'clicado' not in st.session_state:
    st.session_state.clicado = False

# Conteúdo Inicial
st.title("❤️ Para meu amor, minha Lady")
st.markdown(f"### Já estamos juntos há {dias_juntos} dias de pura conexão.")
st.write("---")
st.markdown("""
### Você deixa tudo mais bonito:
Às vezes, a vida nos presenteia de maneira que não entendemos. 
Cada detalhe, cada momento compartilhado com você é uma melodia suave.
""")

# Botão
if st.button("Clique aqui"):
    st.session_state.clicado = True

# O vídeo e as mensagens só aparecem se 'clicado' for True
if st.session_state.clicado:
    st.markdown("<h1 style='text-align: left;'>❤️ ❤️ ❤️ </h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.video('0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4') 
        
    st.success("Você aquece meu coração!")
    st.success("Para sempre vou te amar.")
