import streamlit as app

app.markdown(
    """
    <style>
    /* Target the base document layout, text fields, and markdown tags */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"] p {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    
    /* Target widgets, button components, and subheaders specifically */
    .stButton, .stSelectbox, .stTextInput, h1, h2, h3, h4, h5, h6 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# DESIGN

app.title("imprint oficial")


col1, col2, col3, col4 = app.columns([1, 1, 1, 5])
with col1:
  app.badge(icon="⏱", label="ᴀᴘʟɪᴄᴀᴄɪóɴ 24/7", color="green")
with col2:
  app.badge(icon="🥾", label="ᴇɴᴛʀᴇɢᴀꜱ ʀáᴘɪᴅᴀꜱ")
with col3:
  app.badge(icon="🛡", label="ᴘʀɪᴠᴀᴄɪᴅᴀᴅ ᴍáxɪᴍᴀ")

app.write("Bienvenido a la **página web oficial de Imprint**. Desde aquí, puedes hacer pedidos,\nver nuestro catálogo de productos y ordenar **impresiones 3D personalizadas mediante un archivo específico .STL o .OBJ.**\nAdicionalmente, si no te interesa nuestro catálogo, **puedes buscar más modelos en makerworld.com** con una variedad más amplia de modelos 3D.")