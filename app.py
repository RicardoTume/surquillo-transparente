import streamlit as st
import pandas as pd

st.set_page_config(page_title="PerúDigital", layout="centered")

# MENÚ
st.sidebar.title("PerúDigital")
menu = st.sidebar.radio(
    "Navegación",
    ["Dashboard", "Registro", "Panel", "Agenda", "Transparencia"]
)
# ---------------- DASHBOARD ----------------
if menu == "Dashboard":

    # CABECERA (LA TUYA)
    st.title("Perú Digital")
    st.caption("Hacemos política digital: escuchar, organizar y decidir con datos")

    st.info("Esta plataforma recoge información ciudadana para tomar decisiones basadas en evidencia, no en intuición.")

    # DASHBOARD
    st.subheader("📊 Lo que el país está diciendo ahora")

    try:
        df = pd.read_excel("base_nacional.xlsx")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Personas registradas", len(df))

        with col2:
            tema_top = df["Tema"].value_counts().idxmax()
            st.metric("Tema más importante", tema_top)

        st.subheader("Ranking de problemas")
        ranking = df["Tema"].value_counts()
        st.bar_chart(ranking)

    except:
        st.info("Aún no hay datos. Sé el primero en participar 👇")
        # ---------------- REGISTRO ----------------
elif menu == "Registro":
    st.header("Participa")

    nombre = st.text_input("Nombre")
    telefono = st.text_input("Teléfono")
    departamento = st.text_input("Departamento")
    distrito = st.text_input("Distrito")

    tema = st.selectbox(
        "¿Qué problema te afecta más hoy?",
        ["Seguridad", "Empleo", "Salud", "Educación", "Limpieza", "Transporte"]
    )

    opcion = st.selectbox(
        "¿Qué tan dispuesto estás a participar?",
        [
            "Solo quiero informarme",
            "Me interesa participar ocasionalmente",
            "Me gustaría asistir a una reunión",
            "Quiero apoyar activamente"
        ]
    )

    st.caption("Esto nos ayuda a enviarte solo lo que te interese.")

    if st.button("Guardar"):
        nuevo = pd.DataFrame(
            [[nombre, telefono, departamento, distrito, tema, opcion]],
            columns=["Nombre", "Telefono", "Departamento", "Distrito", "Tema", "Apoyo"]
        )

        try:
            df = pd.read_excel("base_nacional.xlsx")
            df = pd.concat([df, nuevo], ignore_index=True)
        except:
            df = nuevo

        df.to_excel("base_nacional.xlsx", index=False)
        st.success("Registro guardado correctamente")

# ---------------- PANEL ----------------
elif menu == "Panel":
    st.header("Resumen político")

    try:
        df = pd.read_excel("base_nacional.xlsx")

        st.write("Total registrados:", len(df))

        st.subheader("Temas")
        st.bar_chart(df["Tema"].value_counts())

        st.subheader("Nivel de participación")
        st.bar_chart(df["Apoyo"].value_counts())

    except:
        st.warning("Aún no hay datos registrados")

# ---------------- AGENDA ----------------
elif menu == "Agenda":
    st.header("Agenda pública")

    st.write("Sábado: reunión vecinal")
    st.write("Domingo: campaña de salud")

# ---------------- TRANSPARENCIA ----------------
elif menu == "Transparencia":
    st.header("Transparencia")

    data = {
        "Concepto": ["Donaciones", "Materiales", "Eventos"],
        "Monto": [500, -200, -150]
    }

    df = pd.DataFrame(data)
    st.table(df)
