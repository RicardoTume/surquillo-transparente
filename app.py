import streamlit as st
import pandas as pd

st.set_page_config(page_title="Surquillo Transparente")

st.title("Surquillo Transparente")
st.write("Participación y transparencia en un clic")

menu = st.sidebar.selectbox("Menú", ["Registro", "Agenda", "Transparencia"])

if menu == "Registro":
    st.header("Registro ciudadano")

    nombre = st.text_input("Nombre")
    zona = st.selectbox("Zona", ["Surquillo Viejo", "Edificios Nuevos"])
    tema = st.selectbox("Tema", ["Seguridad", "Empleo", "Salud", "Educación"])
    apoyo = st.slider("Nivel de apoyo", 1, 5)

    if st.button("Guardar"):
        nuevo = pd.DataFrame([[nombre, zona, tema, apoyo]],
                             columns=["Nombre", "Zona", "Tema", "Apoyo"])
        try:
            df = pd.read_excel("base_surquillo.xlsx")
            df = pd.concat([df, nuevo], ignore_index=True)
        except:
            df = nuevo

        df.to_excel("base_surquillo.xlsx", index=False)
        st.success("Registro guardado")

elif menu == "Agenda":
    st.header("Agenda pública")
    st.write("Sábado: reunión vecinal")
    st.write("Domingo: campaña de salud")

elif menu == "Transparencia":
    st.header("Transparencia")

    data = {
        "Concepto": ["Donaciones", "Materiales", "Eventos"],
        "Monto": [500, -200, -150]
    }

    df = pd.DataFrame(data)
    st.table(df)