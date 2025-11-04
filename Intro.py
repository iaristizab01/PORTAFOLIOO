import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio de Interfaces - Hora de Aventura",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

st.title("🌟 Portafolio de Interfaces - Hora de Aventura 🌈")
st.markdown("Explora el multiverso creativo de **Isabela Aristizábal**, donde cada interfaz es una aventura en la Tierra de Ooo 🗺️.")

with st.sidebar:
    st.image("images/5d77f80ae9cb39ad03ecbcfc57faf60472-31-ice-king.rsocial.w1200.webp", caption="Rey Helado en su laboratorio", use_container_width=True)
    st.subheader("🧠 Inteligencia Artificial en Acción")
    st.write("La IA nos permite crear, jugar y explorar como nunca antes. ¡Aventúrate a descubrir sus poderes mágicos!")
    st.markdown("🎨 *Diseño y desarrollo por Isabela A.*")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🚀 Intro")
    st.image("images/8d9cf1e90cfd2d6d01274c162e31cf460e8ccc92b4b8c18c7c44fc26257ad331._SX1080_FMjpg_.jpg", width=220)
    st.markdown("[Ver app 🌟](https://qfb9xnb6vchfjzd7p2wvm9.streamlit.app/)")

    st.subheader("🧠 Reconocimiento de Objeto (YOLO)")
    st.image("images/219-2190169_princess-bubblegum-candy-princess-adventure-time.jpg", width=220)
    st.markdown("[Ver app 🔍](https://yolov5-n9zqkkaqi3pouqszrxf38i.streamlit.app/)")

    st.subheader("🎨 ORÁCULO (Reconocimiento de Bocetos)")
    st.image("images/286-2861025_fionna-vector-drawing-by-otownflyer-fiona-from-adventure-time.jpg", width=220)
    st.markdown("[Ver app ✏️](https://historias-nbvxgi6jf6ch7pkpxpqtni.streamlit.app/)")

    st.subheader("📋 Interfaz Táctil (Tablero Personalizado)")
    st.image("images/412-4122478_transparent-adventure-time-characters-png-adventure-time-characters.png", width=220)
    st.markdown("[Ver app 🖐️](https://tablero-dbn5hehsx8wrnj66baepvg.streamlit.app/)")

with col2:
    st.subheader("📚 Análisis de Texto (Inglés)")
    st.image("images/692-6926180_transparent-inhaler-clipart-adventure-time-flying-characters-hd.png", width=220)
    st.markdown("[Ver app 🇬🇧](https://antexttt-mjf27aqsmv8u76w9pq4qtr.streamlit.app/)")

    st.subheader("📖 Análisis de Texto (Español)")
    st.image("images/1750388-rainicorn.webp", width=220)
    st.markdown("[Ver app 🇪🇸](https://antexto06-m2rzpsmhngexyitsywjfnf.streamlit.app/)")

    st.subheader("💬 Chatpat (Sistema Experto LLM)")
    st.image("images/b0d4cc5492d8d905d82e441f7ab8c445.jpg", width=220)
    st.markdown("[Ver app 🤖](https://chatpatpdf-kwfjucahcchusmrf4trxd8.streamlit.app/)")

    st.subheader("🪄 Interpretación de Imagen (LLM)")
    st.image("images/bca0c83812cf80ef385886348519bc8a.jpg", width=220)
    st.markdown("[Ver app 🧠](https://interpretacionimg-appnfeappygwdeqymytkezom.streamlit.app/)")

with col3:
    st.subheader("⚡ Control MQTT (Botones)")
    st.image("images/CakeJS.webp", width=220)
    st.markdown("[Ver app 🔘](https://sistemasiot-zxcfpie4motsgphdhggil4.streamlit.app/)")

    st.subheader("🎙️ Control MQTT (Voz)")
    st.image("images/f1002002b67c44c5b270a616caac3d7f.jpg", width=220)
    st.markdown("[Ver app 🎤](https://ctrlvoice-djxh9psjhlkdqdtjamuetm.streamlit.app/)")

    st.subheader("🧾 Interfaz OCR")
    st.image("images/LSP%27s_Phone.webp", width=220)
    st.markdown("[Ver app 📄](https://xa5vblnqwqtfegqumkrlsk.streamlit.app/)")

    st.subheader("🤲 Reconocimiento de Gestos (Teachable Machine)")
    st.image("images/marceline-is-best-adventure-time-character-v0-wykgmlp7pvzd1.webp", width=220)
    st.markdown("[Ver app ✋](https://recongestos-qulswrztg3uqi9wjyz7r3w.streamlit.app/)")

    st.subheader("💖 Análisis de Sentimiento")
    st.image("images/sub-buzz-4977-1668373544-3.webp", width=220)
    st.markdown("[Ver app 💌](https://icr9cbjgn9ntpknmvorubn.streamlit.app/)")

    st.subheader("🗣️ Traductor Voz - Texto")
    st.image("images/open-discussion-about-the-most-hated-characters-ill-say-v0-uzptbetm33ssa1.webp", width=220)
    st.markdown("[Ver app 🌍](https://traductor-h47sqyeutnj9co4gdmazmv.streamlit.app/)")
