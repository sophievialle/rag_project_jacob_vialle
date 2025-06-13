import streamlit as st
import pandas as pd

# --- Fonctions fictives selon le framework ---
def process_with_langchain(files, question, k, language):
    return f"[LangChain] Réponse en {language} à la question : '{question}' (k={k})"

def process_with_llamaindex(files, question, k, language):
    return f"[LlamaIndex] Réponse en {language} à la question : '{question}' (k={k})"

def main():
    st.title("Analyse de documents")
    st.subheader("Ce texte explique comment fonctionne l'application.")

    # --- Choix du framework ---
    framework = st.radio(
        "Choisissez le framework d'indexation :",
        options=["langchain", "llamaindex"]
    )

    # --- Téléversement de fichiers ---
    uploaded_files = st.file_uploader(
        label="Déposez vos fichiers ici ou chargez-les",
        type=None,
        accept_multiple_files=True
    )
    
    if uploaded_files:
        file_info = []
        for f in uploaded_files:
            size_in_kb = len(f.getvalue()) / 1024
            file_info.append({
                "Nom du fichier": f.name,
                "Taille (KB)": f"{size_in_kb:.2f}"
            })
        df = pd.DataFrame(file_info)
        st.table(df)

    # --- Entrée utilisateur : question ---
    question = st.text_input("Votre question ici")

    # --- Choix de k documents ---
    k = st.slider("Nombre de documents à récupérer", min_value=1, max_value=10, value=3)

    # --- Choix de la langue ---
    language_options = {
        "Français": "fr",
        "Anglais": "en",
        "Espagnol": "es",
        "Allemand": "de"
    }
    language_label = st.selectbox("Choisissez la langue de réponse :", list(language_options.keys()))
    selected_language = language_options[language_label]

    # --- Bouton d'analyse ---
    if st.button("Analyser"):
        if framework == "langchain":
            response = process_with_langchain(uploaded_files, question, k, selected_language)
        else:
            response = process_with_llamaindex(uploaded_files, question, k, selected_language)

        st.text_area("Zone de texte, réponse du modèle", value=response, height=200)

        # --- Feedback utilisateur ---
        feedback = st.radio(
            "Notez la qualité de la réponse (1 = Mauvais, 5 = Excellent) :",
            options=[1, 2, 3, 4, 5]
        )
        if feedback:
            print(f"Feedback utilisateur : {feedback}")
    else:
        st.text_area("Zone de texte, réponse du modèle", value="", height=200)

if __name__ == "__main__":
    main()
