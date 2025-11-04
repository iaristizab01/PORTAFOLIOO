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
        st.warning(f"No se pudo cargar la imagen: {path}")

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
    safe_image("images/a.jpg", caption="Finn y Jake en acción", width=250)
    st.subheader("🧠 Inteligencia Artificial en Acción")
    st.write("La IA nos permite crear, jugar y explorar como nunca antes. ¡Aventúrate a descubrir sus poderes mágicos!")
    st.markdown("🎨 *Diseño y desarrollo por Isabela A.*")

# --- COLUMNAS ---
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    st.subheader("🚀 Intro")
    safe_image("images/b.jpg")
    st.markdown("[Ver app 🌟](https://qfb9xnb6vchfjzd7p2wvm9.streamlit.app/)")

    st.subheader("🧠 Reconocimiento de Objeto (YOLO)")
    safe_image("images/c.jpg")
    st.markdown("[Ver app 🔍](https://yolov5-n9zqkkaqi3pouqszrxf38i.streamlit.app/)")

    st.subheader("🎨 ORÁCULO (Reconocimiento de Bocetos)")
    safe_image("images/d.jpg")
    st.markdown("[Ver app ✏️](https://historias-nbvxgi6jf6ch7pkpxpqtni.streamlit.app/)")

    st.subheader("📋 Interfaz Táctil (Tablero Personalizado)")
    safe_image("images/e.jpg")
    st.markdown("[Ver app 🖐️](https://tablero-dbn5hehsx8wrnj66baepvg.streamlit.app/)")

# --- COLUMNA 2 ---
with col2:
    st.subheader("📚 Análisis de Texto (Inglés)")
    safe_image("images/f.jpg")
    st.markdown("[Ver app 🇬🇧](https://antexttt-mjf27aqsmv8u76w9pq4qtr.streamlit.app/)")

    st.subheader("📖 Análisis de Texto (Español)")
    safe_image("images/g.jpg")
    st.markdown("[Ver app 🇪🇸](https://antexto06-m2rzpsmhngexyitsywjfnf.streamlit.app/)")

    st.subheader("💬 Chatpat (Sistema Experto LLM)")
    safe_image("images/h.jpg")
    st.markdown("[Ver app 🤖](https://chatpatpdf-kwfjucahcchusmrf4trxd8.streamlit.app/)")

    st.subheader("🪄 Interpretación de Imagen (LLM)")
    safe_image("images/i.png")
    st.markdown("[Ver app 🧠](https://interpretacionimg-appnfeappygwdeqymytkezom.streamlit.app/)")

# --- COLUMNA 3 ---
with col3:
    st.subheader("⚡ Control MQTT (Botones)")
    safe_image("images/j.png")
    st.markdown("[Ver app 🔘](https://sistemasiot-zxcfpie4motsgphdhggil4.streamlit.app/)")

    st.subheader("🎙️ Control MQTT (Voz)")
    safe_image("images/k.jpg")
    st.markdown("[Ver app 🎤](https://ctrlvoice-djxh9psjhlkdqdtjamuetm.streamlit.app/)")

    st.subheader("🧾 Interfaz OCR")
    safe_image("images/l.jpg")
    st.markdown("[Ver app 📄](https://xa5vblnqwqtfegqumkrlsk.streamlit.app/)")

    st.subheader("🤲 Reconocimiento de Gestos (Teachable Machine)")
    safe_image("images/m.jpg")
    st.markdown("[Ver app ✋](https://recongestos-qulswrztg3uqi9wjyz7r3w.streamlit.app/)")

    st.subheader("💖 Análisis de Sentimiento")
    safe_image("images/n.png")
    st.markdown("[Ver app 💌](https://icr9cbjgn9ntpknmvorubn.streamlit.app/)")

    st.subheader("🗣️ Traductor Voz - Texto")
    safe_image("images/a.jpg")
    st.markdown("[Ver app 🌍](https://traductor-h47sqyeutnj9co4gdmazmv.streamlit.app/)")
