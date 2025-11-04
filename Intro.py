import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN ---
st.set_page_config(
    page_title="Portafolio de Interfaces - Hora de Aventura",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNCIÓN SEGURA PARA CARGAR IMÁGENES ---
def safe_image(path, caption="", width=220):
    try:
        img = Image.open(path)
        st.image(img, caption=caption, width=width)
    except Exception:
        st.image("images/412-4122478_transparent-adventure-time-characters-png-adventure-time-characters.png",
                 caption="(Imagen no encontrada, placeholder)", width=width)

# --- ESTILOS ---
st.markdown("""
<style>
body {
    background-color: #FFFCEB;
    color: #2A2A2A;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.sidebar .sidebar-content {
    background-color: #FFEBB7;
}
h1, h2, h3, h4 {
    color: #007A73;
    text-shadow: 1px 1px 0px #FFD166;
}
a { color: #008080; font-weight: bold; }
a:hover { color: #FF6F61; }
img { border-radius: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15); }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🌟 Portafolio de Interfaces - Hora de Aventura 🌈")
st.markdown("Explora el multiverso creativo de **Isabela Aristizábal**, donde cada interfaz es una aventura diferente en la Tierra de Ooo 🗺️.")

# --- SIDEBAR ---
with st.sidebar:
    safe_image("images/71xHh6f9YgL._AC_UF1000,1000_QL80_.jpg", caption="Finn y Jake en acción", width=250)
    st.subheader("🧠 Inteligencia Artificial en Acción")
    st.write("La IA nos permite crear, jugar y explorar como nunca antes. ¡Aventúrate a descubrir sus poderes mágicos!")
    st.markdown("🎨 *Diseño y desarrollo por Isabela A.*")

# --- COLUMNAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    st.subheader("🚀 Intro")
    safe_image("images/l-intro-1617997359.jpg")
    st.markdown("[Ver app 🌟](https://qfb9xnb6vchfjzd7p2wvm9.streamlit.app/)")

    st.subheader("🧠 Reconocimiento de Objeto (YOLO)")
    safe_image("images/219-2190169_princess-bubblegum-candy-princess-adventure-time.jpg")
    st.markdown("[Ver app 🔍](https://yolov5-n9zqkkaqi3pouqszrxf38i.streamlit.app/)")

    st.subheader("🎨 ORÁCULO (Reconocimiento de Bocetos)")
    safe_image("images/286-2861025_fionna-vector-drawing-by-otownflyer-fiona-from-adventure-time.jpg")
    st.markdown("[Ver app ✏️](https://historias-nbvxgi6jf6ch7pkpxpqtni.streamlit.app/)")

    st.subheader("📋 Interfaz Táctil (Tablero Personalizado)")
    safe_image("images/adventure-time-cake-the-cat.png")
    st.markdown("[Ver app 🖐️](https://tablero-dbn5hehsx8wrnj66baepvg.streamlit.app/)")

# --- COLUMNA 2 ---
with col2:
    st.subheader("📚 Análisis de Texto (Inglés)")
    safe_image("images/8d9cf1e90cfd2d6d01274c162e31cf460e8ccc92b4b8c18c7c44fc26257ad331._SX1080_FMjpg_.jpg")
    st.markdown("[Ver app 🇬🇧](https://antexttt-mjf27aqsmv8u76w9pq4qtr.streamlit.app/)")

    st.subheader("📖 Análisis de Texto (Español)")
    safe_image("images/b0d4cc5492d8d905d82e441f7ab8c445.jpg")
    st.markdown("[Ver app 🇪🇸](https://antexto06-m2rzpsmhngexyitsywjfnf.streamlit.app/)")

    st.subheader("💬 Chatpat (Sistema Experto LLM)")
    safe_image("images/f1002002b67c44c5b270a616caac3d7f.jpg")
    st.markdown("[Ver app 🤖](https://chatpatpdf-kwfjucahcchusmrf4trxd8.streamlit.app/)")

    st.subheader("🪄 Interpretación de Imagen (LLM)")
    safe_image("images/bca0c83812cf80ef385886348519bc8a.jpg")
    st.markdown("[Ver app 🧠](https://interpretacionimg-appnfeappygwdeqymytkezom.streamlit.app/)")

# --- COLUMNA 3 ---
with col3:
    st.subheader("⚡ Control MQTT (Botones)")
    safe_image("images/412-4122478_transparent-adventure-time-characters-png-adventure-time-characters.png")
    st.markdown("[Ver app 🔘](https://sistemasiot-zxcfpie4motsgphdhggil4.streamlit.app/)")

    st.subheader("🎙️ Control MQTT (Voz)")
    safe_image("images/692-6926180_transparent-inhaler-clipart-adventure-time-flying-characters-hd.png")
    st.markdown("[Ver app 🎤](https://ctrlvoice-djxh9psjhlkdqdtjamuetm.streamlit.app/)")

    st.subheader("🧾 Interfaz OCR")
    safe_image("images/is-it-me-or-does-marceline-look-different-as-the-series-v0-wmaumw5d3uh3b1.jpg")
    st.markdown("[Ver app 📄](https://xa5vblnqwqtfegqumkrlsk.streamlit.app/)")

    st.subheader("🤲 Reconocimiento de Gestos (Teachable Machine)")
    safe_image("images/da19b91522a87825e03d47f903838e66.jpg")
    st.markdown("[Ver app ✋](https://recongestos-qulswrztg3uqi9wjyz7r3w.streamlit.app/)")

    st.subheader("💖 Análisis de Sentimiento")
    safe_image("images/Screenshot-2023-06-08-144133.jpg")
    st.markdown("[Ver app 💌](https://icr9cbjgn9ntpknmvorubn.streamlit.app/)")

    st.subheader("🗣️ Traductor Voz - Texto")
    safe_image("images/marceline-is-best-adventure-time-character-v0-wykgmlp7pvzd1.jpg")
    st.markdown("[Ver app 🌍](https://traductor-h47sqyeutnj9co4gdmazmv.streamlit.app/)")
