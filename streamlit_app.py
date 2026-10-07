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

with col1:
    with st.container(border=True):
        # Imatge del producte (pots fer servir un enllaç d'Internet o una ruta local)
        st.image("https://placehold.co", use_container_width=True)
        
        # Text del producte
        st.subheader("Producte A")
        st.write("**Preu:** 19,99 €")
        st.write("Aquesta és una descripció breu i atractiva del Producte A.")
        
        # Botó d'acció
        if st.button("Comprar A", key="btn_a"):
            st.success("S'ha afegit el Producte A al carret!")

# --- PRODUCTE 2 ---
with col2:
    with st.container(border=True):
        st.image("https://placehold.co", use_container_width=True)
        
        st.subheader("Producte B")
        st.write("**Preu:** 29,99 €")
        st.write("Aquesta és una descripció breu i atractiva del Producte B.")
        
        if st.button("Comprar B", key="btn_b"):
            st.success("S'ha afegit el Producte B al carret!")

# --- PRODUCTE 3 ---
with col3:
    with st.container(border=True):
        st.image("https://placehold.co", use_container_width=True)
        
        st.subheader("Producte C")
        st.write("**Preu:** 39,99 €")
        st.write("Aquesta és una descripció breu i atractiva del Producte C.")
        
        if st.button("Comprar C", key="btn_c"):
            st.success("S'ha afegit el Producte C al carret!")