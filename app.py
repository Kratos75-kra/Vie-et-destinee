
import streamlit as st
from datetime import datetime

# === FONCTIONS DE NUMÉROLOGIE ===
def calcul_chemin_de_vie(date_naissance):
    chiffres = [int(c) for c in date_naissance if c.isdigit()]
    total = sum(chiffres)
    while total > 9 and total not in [11, 22, 33]:
        total = sum([int(c) for c in str(total)])
    return total

def interpretation_chemin(chemin):
    interpretations = {
        1: "Leader né, vous êtes indépendant, ambitieux et capable d'ouvrir de nouveaux chemins.",
        2: "Maître diplomate, vous excellez dans la coopération et la médiation.",
        3: "Communicant créatif, vous brillez par votre expression, votre optimisme et votre talent.",
        4: "Travailleur organisé, vous construisez avec patience, logique et rigueur.",
        5: "Esprit libre, vous êtes aventureux, curieux et aimez le changement.",
        6: "Porteur d'harmonie, vous protégez les autres avec amour, responsabilité et équilibre.",
        7: "Chercheur de vérité, vous êtes introspectif, analytique et spirituel.",
        8: "Maître du pouvoir et de la réussite matérielle, vous visez l'accomplissement.",
        9: "Serviteur de l'humanité, vous portez une vibration d'amour universel et de sagesse.",
        11: "Maître spirituel, vous avez une intuition puissante et une mission de guide.",
        22: "Grand constructeur, vous êtes capable de réaliser des projets de grande ampleur.",
        33: "Maître enseignant, vous portez une vibration d'amour inconditionnel et de service global."
    }
    return interpretations.get(chemin, "Aucune interprétation disponible.")

# === INTERFACE STREAMLIT ===
st.set_page_config(page_title="Vie et Destinée ✨", page_icon="✨")

# Bannière (image URL libre ou base64 pour plus tard)
st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://i.imgur.com/WxNc92E.png" alt="Vie et Destinée" width="200" />
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:#6A0DAD; text-align:center;'>💫 Vie et Destinée</h1>", unsafe_allow_html=True)
st.markdown("---")

nom = st.text_input("Entrez votre nom complet")
date_naissance = st.date_input("Choisissez votre date de naissance", format="YYYY-MM-DD")

if st.button("Analyser ma date de naissance"):
    if not nom.strip():
        st.warning("Merci d'entrer votre nom complet pour une expérience personnalisée.")
    else:
        chemin = calcul_chemin_de_vie(date_naissance.strftime("%Y%m%d"))
        interpretation = interpretation_chemin(chemin)

        st.markdown(f"### Bonjour, {nom.split()[0].capitalize()} !")
        st.subheader(f"🔢 Votre chiffre de chance : {chemin}")
        st.markdown(f"**Mission de vie :** {interpretation}")

        st.info(
            "Pour une analyse spirituelle plus avancée incluant chiromancie, astrologie et numérologie complète, "
            "débloquez la version premium prochainement !"
        )

st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:0.8em; color:gray;'>© 2025 Vie et Destinée - Tous droits réservés</p>",
    unsafe_allow_html=True,
)
