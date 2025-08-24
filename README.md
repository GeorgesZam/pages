
# Streamlit sur GitHub Pages (stlite) — Template prêt à forker

Ce template vous permet d'exécuter **Streamlit dans le navigateur** (via **[stlite](https://github.com/whitphx/stlite)** + Pyodide) et de **déployer statiquement sur GitHub Pages**.
👉 Chacun peut proposer des modifications via **Pull Requests**. Les PR obtiennent des **prévisualisations de déploiement** automatiques.

## 🔥 Pourquoi ce setup ?
- **Scalable par défaut** : GitHub Pages est servi par un CDN mondial.
- **Sans serveur** : aucune infra à gérer. Python tourne *dans* le navigateur (WASM).
- **Fork‑friendly** : tout le monde peut forker/PR votre app (`app.py`).

## 🚀 Démarrage rapide
1. **Forkez** ce repo.
2. Activez **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Poussez sur `main`. Une fois le workflow vert, votre site est en ligne : `https://<votre-user>.github.io/<repo>/`

> ⚠️ Localement, servez les fichiers via un petit serveur web (sinon `fetch('app.py')` échoue en `file://`).  
> Exemple : `python -m http.server 8000` puis ouvrez `http://localhost:8000`

## 🧩 Modifier l'app
- Éditez **`app.py`** → commit → push → Pages se redéploie.
- Ajoutez des dépendances **pures Python** dans `requirements.txt` (compatibles Pyodide).
  - Les libs avec extensions natives (C/C++) ne fonctionneront pas ici.

## 🧱 Structure
```text
.
├─ index.html                 # charge stlite et lit app.py/requirements.txt
├─ app.py                     # votre app Streamlit
├─ requirements.txt           # (optionnel) paquets Python purs (wheels/py) pour Pyodide
├─ .streamlit/config.toml     # thème Streamlit
└─ .github/workflows/pages.yml# déploiement auto sur Pages (PR previews)
```

## ⚡ Aller plus loin (vraiment scalable & lourd)
- **Backend serverless** (Cloudflare Workers, FastAPI sur Fly.io/Render, etc.) exposant des endpoints.  
  L'app (stlite) appelle ces endpoints pour les tâches lourdes (IA, DB, etc.).
- **Mode hybride** : gardez ce site (Pages) **+** déployez la version Python complète sur Streamlit Community Cloud / Hugging Face Spaces.

---

© Vous. Bon hack !
