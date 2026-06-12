import streamlit as st
import base64
import time
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Para você", page_icon="❤️")

# --- Função para carregar a imagem de fundo ---
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

# Defina aqui o nome exato do seu arquivo de imagem
set_bg_hack('foto.jpg') 

# --- Conteúdo da Página ---
st.title("❤️ Para meu amor, minha Lady")
st.write("---")

# Espaço reservado para o contador em tempo real
placeholder = st.empty()

# Cálculo do tempo (Data inicial 15/09/2025)
data_inicio = datetime(2025, 9, 15, 0, 0, 0)
agora = datetime.now()
delta = agora - data_inicio

dias = delta.days
segundos_totais = delta.seconds
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

# Mostra o contador
placeholder.markdown(f"""
### Já estamos juntos há:
# {dias} dias, {horas}h, {minutos}m e {segundos}s de conexão.
""")

st.markdown("""
### Você deixa tudo mais bonito:
Às vezes, a vida nos presenteia de maneira que não entendemos. 
Cada detalhe, cada momento compartilhado com você é uma melodia suave.
""")

# --- Lógica do Botão ---
if 'clicado' not in st.session_state:
    st.session_state.clicado = False

if st.button("Clique aqui"):
    st.session_state.clicado = True

if st.session_state.clicado:
    st.markdown("<h1 style='text-align: left;'>❤️ ❤️ ❤️ </h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Defina aqui o nome exato do seu arquivo de vídeo
        st.video('0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4') 
        
    st.success("Você aquece meu coração!")
    st.success("Para sempre vou te amar.")

# Atualiza a página a cada 1 segundo para o contador de segundos rodar
time.sleep(1)
st.rerun()
