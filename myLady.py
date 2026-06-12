import streamlit as st
import base64
import time
from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo
from zoneinfo import ZoneInfo

tz = ZoneInfo("America/Sao_Paulo")

# Hora atual
agora = datetime.now(tz)

dias = agora.day
horas = agora.hour
minutos = agora.minute
segundos = agora.second

# Mostra no mesmo formato
placeholder.markdown(f"""
### Já estamos juntos há:
# {dias} dias, {horas}h, {minutos}m e {segundos}s de conexão.
""")
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

# --- Conteúdo da Página ---
st.title("❤️ Para meu amor, minha Lady")
st.write("---")

# Espaço reservado para o contador
placeholder = st.empty()

data_inicio = datetime(2025, 9, 15, 0, 0, 0)
agora = datetime.now()

delta = agora - data_inicio

total_segundos = int(delta.total_seconds())

dias = total_segundos // 86400
horas = (total_segundos % 86400) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

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
        st.video('0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4') 
        
    st.success("Você aquece meu coração!")
    st.success("Para sempre vou te amar.")

# Para o contador atualizar sem recarregar manualmente, usamos o rerun
time.sleep(1)
st.rerun()
