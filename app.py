
import streamlit as st
from datetime import datetime
from functools import lru_cache

st.set_page_config(page_title="Template Streamlit (GitHub Pages + stlite)", page_icon="🧊", layout="wide")

st.title("🚀 Streamlit sur GitHub Pages (stlite)")
st.caption("Modèle prêt à forker – éditez `app.py` et poussez sur GitHub : le site se met à jour automatiquement.")

with st.sidebar:
    st.header("🔧 Paramètres")
    name = st.text_input("Votre nom", value="Georges")
    dark = st.toggle("Mode sombre (préférence navigateur)")
    st.markdown("---")
    st.markdown("**Contribuer** : proposez des idées dans les Issues ou ouvrez une Pull Request.")

st.success(f"Bienvenue, **{name}** !")

tab1, tab2, tab3 = st.tabs(["🗂️ Démo", "📎 Fichiers", "⚡ Cache / Performance"])

with tab1:
    st.subheader("Composants de base")
    col1, col2 = st.columns(2)
    with col1:
        txt = st.text_area("Saisissez du texte", "Hello, Streamlit on Pages!")
        st.write("Longueur :", len(txt))
        uploaded = st.file_uploader("Uploader un fichier (local / navigateur)", type=None)
        if uploaded is not None:
            st.write("Nom :", uploaded.name, "Taille:", uploaded.size, "octets")
            st.download_button("Télécharger tel quel", data=uploaded.getvalue(), file_name=uploaded.name)
    with col2:
        st.slider("Un slider 👇", 0, 100, 42)
        st.checkbox("Une checkbox")
        st.radio("Un radio", ["A", "B", "C"], index=1)

    st.info("💡 Ce template tourne **entièrement dans le navigateur** via Pyodide. "
            "Idéal pour un déploiement statique, forkable et ultra-scalable via le CDN de GitHub Pages.")

with tab2:
    st.subheader("Structure du projet")
    st.code(
        """
        .
        ├─ index.html                 # charge stlite et lit app.py/requirements.txt
        ├─ app.py                     # votre app Streamlit
        ├─ requirements.txt           # (optionnel) paquets Python purs (wheels/py) pour Pyodide
        ├─ .streamlit/config.toml     # thème Streamlit
        └─ .github/workflows/pages.yml# déploiement auto sur Pages
        """, language="text"
    )
    st.markdown(
        "- **Forkez** le repo → **éditez `app.py`** → **push** → **Pages déploie** automatiquement.\n"
        "- Ouvrez des **PR** : l'action génère des **préviews** de déploiement."
    )

@lru_cache(maxsize=32)
def heavy_compute(n: int) -> int:
    # Démo CPU (synchrone) – dans stlite, évitez les calculs trop lourds.
    s = 0
    for i in range(n * 10_000):
        s += (i % 7) * (i % 13)
    return s

with tab3:
    st.subheader("Cache / Performance")
    n = st.number_input("Paramètre de calcul", min_value=1, max_value=200, value=50, step=1)
    if st.button("Calculer"):
        with st.spinner("Calcul en cours…"):
            res = heavy_compute(int(n))
        st.success(f"Résultat: {res}")
        st.caption("⚠️ Pour des workloads lourds, exposez une API (serverless) et appelez-la depuis l'app stlite.")

st.caption(f"🕒 Build: {datetime.utcnow().isoformat()}Z · stlite + GitHub Pages")
