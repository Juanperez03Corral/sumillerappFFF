
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chin Chin: Recomendador creativo de vinos con doble recomendación por plato,
formulario personalizado y selección de regiones vitivinícolas.
"""

import streamlit as st

# Función para recomendar dos vinos por plato
def recomendar_vino(plato, tipo_vino, dulzor, region_favorita):
    vinos_por_plato = {
        "Gazpacho andaluz": [
            {
                "vino": "Pazo de Señoráns Albariño",
                "calidad": "Estándar",
                "explicacion": "Fresco y afrutado, realza el frescor del gazpacho.",
                "copa": 3.5,
                "botella": 25.0
            },
            {
                "vino": "Do Ferreiro Cepas Vellas",
                "calidad": "Alta gama",
                "explicacion": "Más mineral y complejo, ideal para sofisticar este plato.",
                "copa": 6.0,
                "botella": 45.0
            }
        ],
        "Tortilla española": [
            {
                "vino": "Marqués de Murrieta Rioja Reserva",
                "calidad": "Estándar",
                "explicacion": "Con cuerpo, armoniza con la textura de la tortilla.",
                "copa": 5.0,
                "botella": 35.0
            },
            {
                "vino": "La Rioja Alta Gran Reserva 904",
                "calidad": "Alta gama",
                "explicacion": "Elegante y estructurado, eleva el sabor del plato.",
                "copa": 7.5,
                "botella": 60.0
            }
        ]
        # El resto de platos se completará más adelante...
    }

    return vinos_por_plato.get(plato, [])

# --- Interfaz principal ---
st.set_page_config(page_title="Chin Chin 🍷", layout="centered")
st.title("🍷 Chin Chin: Tu Sumiller Virtual")
st.markdown("Explora maridajes únicos y encuentra el vino ideal para tu plato.")

# --- Formulario personalizado ---
with st.form("formulario_usuario"):
    nombre = st.text_input("👤 ¿Cuál es tu nombre?")
    edad = st.number_input("🎂 ¿Qué edad tienes?", min_value=0, step=1)
    genero = st.selectbox("🧑‍🤝‍🧑 ¿Cuál es tu género?", ["Prefiero no decirlo", "Femenino", "Masculino", "Otro"])
    frecuencia = st.selectbox("📅 ¿Con qué frecuencia sueles beber vino?", ["Ocasionalmente", "Semanalmente", "A diario"])
    tipo_vino = st.selectbox("🍇 ¿Qué tipo de vino prefieres?", ["Tinto", "Blanco", "Rosado", "Espumoso", "Me da igual"])
    dulzor = st.selectbox("🍬 ¿Qué nivel de dulzor prefieres?", ["Seco", "Semiseco", "Dulce", "Me da igual"])
    region_favorita = st.selectbox("🌍 Elige una región vitivinícola favorita", [
        "🌿 Ribera del Duero", "🌊 Rías Baixas", "🔥 Priorat", "🌞 La Toscana", "🌬 Borgoña", "🌄 Valle del Napa"
    ])
    plato = st.selectbox("🍽 ¿Qué plato vas a disfrutar?", [
        "Gazpacho andaluz", "Tortilla española", "Ensaladilla rusa", "Almejas a la marinera",
        "Pimientos de padrón", "Paella Valenciana", "Cordero asado al horno",
        "Merluza a la gallega", "Croquetas de jamón ibérico", "Pollo al ajillo"
    ])
    enviar = st.form_submit_button("🔍 Buscar vinos")

if enviar:
    if edad < 18:
        st.warning("🚫 Está prohibida la venta de alcohol a menores de 18 años.")
    else:
        st.success(f"🍷 Recomendaciones para {nombre}:")
        vinos = recomendar_vino(plato, tipo_vino, dulzor, region_favorita)
        if vinos:
            for vino in vinos:
                st.write(f"### {vino['calidad']} – {vino['vino']}")
                st.write(f"📝 {vino['explicacion']}")
                st.write(f"💶 Copa: {vino['copa']} € | Botella: {vino['botella']} €")
                st.markdown("---")
        else:
            st.warning("😕 Aún no tenemos una recomendación para este plato. ¡Pronto la añadiremos!")
