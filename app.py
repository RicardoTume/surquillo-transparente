import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perú Digital")

st.title("Perú Digital")
st.caption("Hacemos política digital: escuchar, organizar y decidir con datos")
st.info("Esta plataforma recoge información ciudadana para tomar decisiones basadas en evidencia, no en intuición.")
menu = st.sidebar.selectbox("Menú", ["Registro", "Agenda", "Transparencia", "Panel"])

if menu == "Registro":
    st.header("Registro ciudadano")

    nombre = st.text_input("Nombre")
    departamento = st.selectbox("Departamento", [
        "Lima", "Arequipa", "Cusco", "Piura", "La Libertad", "Otros"])
    distrito = st.text_input("Distrito")
    tema = st.selectbox("Tema", ["Seguridad", "Empleo", "Salud", "Educación", "Orden", "Limpieza", "Iluminación", "Agua"])
    opcion = st.selectbox(
        "¿Qué tan dispuesto estás a participar con nosotros?",
        [
            "Solo quiero informarme",
            "Me interesa participar ocasionalmente",
            "Me gustaría asisitr a una reunión",
            "Quiero apoyar activamente"
        ]
    )
    st.caption("Esto nos ayuda a enviarte solo lo que te interese.")
    mapa_apoyo = {
        "Solo quiero informarme" : 2,
        "Me interesa participar ocasionalmente" : 3,
        "Me gustaría asisitr a una reunión" : 4,
        "Quiero apoyar activamente" : 5
    }
    apoyo = mapa_apoyo[opcion]
    telefono = st.text_input("Telefono")
    permiso = st.selectbox("¿Acepta ser contactado?", ["Si", "No"])
    observaciones = st.text_area ("Observaciones")

    if st.button("Guardar"):
        nuevo = pd.DataFrame([[nombre, telefono, departamento, distrito, tema, apoyo, permiso, observaciones]],
                             columns=["Nombre", "Telefono", "Departamento", "Distrito", "Tema", "Apoyo", "Permiso", "Observaciones"])
        try:
            df = pd.read_excel("base_nacional.xlsx")
            df = pd.concat([df, nuevo], ignore_index=True)
        except:
            df = nuevo

        df.to_excel("base_nacional.xlsx", index=False)
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
        df = pd.read_excel("base_nacional.xlsx")

        st.write("Total registrados:", len(df))
        st.write("Apoyo promedio:", round(df["Apoyo"].mean(), 2))

        st.subheader("Apoyo por zona")
        st.bar_chart(df.groupby("Departamento")["Apoyo"].mean())

        st.subheader("Temas principales")
        st.bar_chart(df["Tema"].value_counts())

    except:
        st.warning("Aún no hay datos")
