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


col1, col2, col3 = app.columns([1, 1, 1], gap="xsmall")
with col1:
  app.badge(icon="⏱", label="ᴀᴘʟɪᴄᴀᴄɪóɴ 24/7", color="green")
with col2:
  app.badge(icon="🥾", label="ᴇɴᴛʀᴇɢᴀꜱ ʀáᴘɪᴅᴀꜱ")
with col3:
  app.badge(icon="🛡", label="ᴘʀɪᴠᴀᴄɪᴅᴀᴅ ᴍáxɪᴍᴀ", color="orange")

app.write("Bienvenido a la **página web oficial de Imprint**. Desde aquí, puedes hacer pedidos,\nver nuestro catálogo de productos y ordenar **impresiones 3D personalizadas mediante un archivo específico .STL o .OBJ.**\nAdicionalmente, si no te interesa nuestro catálogo, **puedes buscar más modelos en makerworld.com** con una variedad más amplia de modelos 3D.")

app.divider()

col1, col2, col3 = app.columns(3)


with col1:
    with app.container(border=True):
        
        app.image("imatges/banner_makerworld.png", use_container_width=True)
        
        app.subheader("Busca en Makerworld")
        app.badge(label="ACTIVO", icon="🟢")
        app.write("Busca en Makerworld para encontrar más modelos para imprimir")
        
        if app.button("Ir", key="btn_a"):
            app.link_button("Ir a Makerworld", "https://makerworld.com")


with col2:
    with app.container(border=True):
        app.image("https://placehold.co", use_container_width=True)
        
        app.subheader("Producte B")
        app.write("**Preu:** 29,99 €")
        app.write("Aquesta és una descripció breu i atractiva del Producte B.")
        
        if app.button("Ir", key="btn_b"):
            app.success("S'ha afegit el Producte B al carret!")

with col3:
    with app.container(border=True):
        app.image("https://placehold.co", use_container_width=True)
        
        app.subheader("Producte B")
        app.write("**Preu:** 29,99 €")
        app.write("Aquesta és una descripció breu i atractiva del Producte B.")
        
        if app.button("Ir", key="btn_b"):
            app.success("S'ha afegit el Producte B al carret!")