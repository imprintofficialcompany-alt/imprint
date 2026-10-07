import streamlit as app

st.markdown(
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

app.divider()

app.write("Bienvenido a la **página web oficial de Imprint**. Desde aquí, puedes hacer pedidos,\nver nuestro catálogo de productos y ordenar **impresiones 3D personalizadas mediante un archivo específico .STL o .OBJ.**\nAdicionalmente, si no te interesa nuestro catálogo, **puedes buscar más modelos en makerworld.com** con una variedad más amplia de modelos 3D.")