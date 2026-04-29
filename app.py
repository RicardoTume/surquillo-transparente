import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perú Digital")

st.title("Perú Digital")
st.caption("Hacemos política digital: escuchar, organizar y decidir con datos")

menu = st.sidebar.selectbox("Menú", ["Registro", "Agenda", "Transparencia", "Panel"])

if menu == "Registro":
    st.header("Registro ciudadano")

    nombre = st.text_input("Nombre")
    zona = st.selectbox("Zona", ["Surquillo Viejo", "Edificios Nuevos"])
    tema = st.selectbox("Tema", ["Seguridad", "Empleo", "Salud", "Educación"])
    apoyo = st.slider("Nivel de apoyo", 1, 5)
    telefono = st.text_input("Telefono")
    permiso = st.selectbox("¿Acepta ser contactado?", ["Si", "No"])
    observaciones = st.text_area ("Observaciones")

    if st.button("Guardar"):
        nuevo = pd.DataFrame([[nombre, telefono, zona, tema, apoyo, permiso, observaciones]],
                             columns=["Nombre", "Telefono", "Zona", "Tema", "Apoyo", "Permiso", "Observaciones"])
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

elif menu == "Panel":
    st.header("Resumen político")

    try:
        df = pd.read_excel("base_surquillo.xlsx")

        st.write("Total registrados:", len(df))
        st.write("Apoyo promedio:", round(df["Apoyo"].mean(), 2))

        st.subheader("Apoyo por zona")
        st.bar_chart(df.groupby("Zona")["Apoyo"].mean())

        st.subheader("Temas principales")
        st.bar_chart(df["Tema"].value_counts())

    except:
        st.warning("Aún no hay datos")
