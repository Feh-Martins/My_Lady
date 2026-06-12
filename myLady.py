import streamlit as st
import base64
from datetime import datetime

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

# Tente carregar a foto, se der erro, o código não para
try:
    set_bg_hack('foto.jpg')
except:
    st.write("Imagem de fundo não encontrada.")

# --- Conteúdo ---
st.title("❤️ Para meu amor, minha Lady")
st.write("---")

# Cálculo do tempo
data_inicio = datetime(2025, 9, 15, 0, 0, 0)
agora = datetime.now()
delta = agora - data_inicio

dias = delta.days
segundos_totais = delta.seconds
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

# Exibe o contador
st.markdown(f"### Já estamos juntos há: \n# {dias} dias, {horas}h, {minutos}m e {segundos}s.")

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
    
    # Usando o Uploader para evitar o erro de caminho de arquivo
    st.write("Se o vídeo não aparecer, carregue o arquivo abaixo:")
    video_file = st.file_uploader("Escolha o vídeo", type=['mp4'])
    
    if video_file is not None:
        st.video(video_file)
    else:
        # Tenta carregar o arquivo local se o uploader não for usado
        try:
            st.video('0d630c90-92b0-4cc6-982e-fe9b8f36678c-VIDEO_HIGHLIGHT.mp4')
        except:
            st.write("Vídeo não encontrado na pasta.")
        
    st.success("Você aquece meu coração!")
    st.success("Para sempre vou te amar.")

# REMOVIDO o st.rerun() e o time.sleep() para não travar o clique!
