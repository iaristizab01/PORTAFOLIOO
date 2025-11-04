import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portafolio de Interfaces - Hora de Aventura",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS ---
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
a {
    color: #008080;
    font-weight: bold;
}
a:hover {
    color: #FF6F61;
}
img {
    border-radius: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# --- TÍTULO PRINCIPAL ---
st.title("🌟 Portafolio de Interfaces - Hora de Aventura 🌈")
st.markdown("Explora el multiverso creativo de **Isabela Aristizábal**, donde cada interfaz es una aventura distinta en la Tierra de Ooo 🗺️.")

# --- SIDEBAR ---
with st.sidebar:
    st.image("OIG6.jpg", caption="Finn y Jake explorando mundos", use_container_width=True)
    st.subheader("🧠 ¿Qué es la Inteligencia Artificial?")
    st.write("La **IA** nos permite crear, jugar y explorar como nunca antes, combinando magia y tecnología. ¡Aventúrate a descubrirla!")
    st.markdown("---")
    st.markdown("🎨 *Diseño y desarrollo por Isabela A.*")

# --- COLUMNAS ---
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    st.subheader("🚀 Intro")
    st.image("https://i.pinimg.com/736x/aa/a3/02/aaa302d1f425657a9b87ef3623175e8e.jpg", width=220)
    st.markdown("[Ver app 🌟](https://qfb9xnb6vchfjzd7p2wvm9.streamlit.app/)")

    st.subheader("🧠 Reconocimiento de Objeto (YOLO)")
    st.image("https://i.pinimg.com/736x/8d/17/3a/8d173a7a223236b61a9de4e81c4223d7.jpg", width=220)
    st.markdown("[Ver app 🔍](https://yolov5-n9zqkkaqi3pouqszrxf38i.streamlit.app/)")

    st.subheader("🎨 ORÁCULO (Reconocimiento de Bocetos)")
    st.image("https://i.pinimg.com/736x/bc/2c/4e/bc2c4e6d087d979c4086f00e75301d40.jpg", width=220)
    st.markdown("[Ver app ✏️](https://historias-nbvxgi6jf6ch7pkpxpqtni.streamlit.app/)")

    st.subheader("📋 Interfaz Táctil (Tablero Personalizado)")
    st.image("https://i.pinimg.com/736x/18/24/0b/18240b9a243b13c7164b3da71a02b0d3.jpg", width=220)
    st.markdown("[Ver app 🖐️](https://tablero-dbn5hehsx8wrnj66baepvg.streamlit.app/)")

# --- COLUMNA 2 ---
with col2:
    st.subheader("📚 Análisis de Texto (Inglés)")
    st.image("https://i.pinimg.com/736x/a7/9e/36/a79e367270d70fc51ac60a210f3f4b70.jpg", width=220)
    st.markdown("[Ver app 🇬🇧](https://antexttt-mjf27aqsmv8u76w9pq4qtr.streamlit.app/)")

    st.subheader("📖 Análisis de Texto (Español)")
    st.image("https://i.pinimg.com/736x/3b/22/cc/3b22cc7d0846bff0b36cc23e6c3a91ab.jpg", width=220)
    st.markdown("[Ver app 🇪🇸](https://antexto06-m2rzpsmhngexyitsywjfnf.streamlit.app/)")

    st.subheader("💬 Chatpat (Sistema Experto LLM)")
    st.image("https://i.pinimg.com/736x/67/d8/b3/67d8b37e5da0b271a5ff8ab88849aaba.jpg", width=220)
    st.markdown("[Ver app 🤖](https://chatpatpdf-kwfjucahcchusmrf4trxd8.streamlit.app/)")

    st.subheader("🪄 Interpretación de Imagen (LLM)")
    st.image("https://i.pinimg.com/736x/79/8b/89/798b89e68b14a05f7b52ed3c326c6026.jpg", width=220)
    st.markdown("[Ver app 🧠](https://interpretacionimg-appnfeappygwdeqymytkezom.streamlit.app/)")

# --- COLUMNA 3 ---
with col3:
    st.subheader("⚡ Control MQTT (Botones)")
    st.image("https://i.pinimg.com/736x/f9/68/10/f968107cd8c0e1f32adf2438d51ac3c8.jpg", width=220)
    st.markdown("[Ver app 🔘](https://sistemasiot-zxcfpie4motsgphdhggil4.streamlit.app/)")

    st.subheader("🎙️ Control MQTT (Voz)")
    st.image("https://i.pinimg.com/736x/d4/4e/19/d44e19c9ab60799685a4ec406c918d7f.jpg", width=220)
    st.markdown("[Ver app 🎤](https://ctrlvoice-djxh9psjhlkdqdtjamuetm.streamlit.app/)")

    st.subheader("🧾 Interfaz OCR")
    st.image("https://i.pinimg.com/736x/9e/a1/35/9ea13545b8e44c857b38847b7d14f682.jpg", width=220)
    st.markdown("[Ver app 📄](https://xa5vblnqwqtfegqumkrlsk.streamlit.app/)")

    st.subheader("🤲 Reconocimiento de Gestos (Teachable Machine)")
    st.image("https://i.pinimg.com/736x/79/91/bb/7991bb067da20f2a836117c23921bb6d.jpg", width=220)
    st.markdown("[Ver app ✋](https://recongestos-qulswrztg3uqi9wjyz7r3w.streamlit.app/)")

    st.subheader("💖 Análisis de Sentimiento")
    st.image("https://i.pinimg.com/736x/ed/5a/57/ed5a57d5c944f84ad226353e8e8e7084.jpg", width=220)
    st.markdown("[Ver app 💌](https://icr9cbjgn9ntpknmvorubn.streamlit.app/)")

    st.subheader("🗣️ Traductor Voz - Texto")
    st.image("https://i.pinimg.com/736x/6c/3e/52/6c3e523bb8e62f36e3efcf03513b4d77.jpg", width=220)
    st.markdown("[Ver app 🌍](https://traductor-h47sqyeutnj9co4gdmazmv.streamlit.app/)")
