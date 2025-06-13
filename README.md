# Analyse de documents avec un RAG

Cette application Streamlit permet d’analyser des documents PDF et de poser des questions en langage naturel sur leur contenu. Elle propose deux frameworks au choix : **LangChain** et **LlamaIndex**, connectés à des modèles OpenAI.

## Fonctionnalités
Les fonctionnalités de l'application sont les suivantes : 
- Téléversement de fichiers PDF
- Choix entre LangChain ou LlamaIndex pour l’indexation
- Interrogation en langage naturel
- Sélection de la langue de réponse (Français, Anglais, Espagnol, Allemand)
- Notation de la qualité des réponses

## Installation

1. Cloner ce dépôt :
   git clone https://github.com/sophievialle/rag_project_jacob_vialle
   cd analyse-docs-streamlit

2. Créer un environnement virtuel et installer les dépendances :
   python -m venv venv
   source venv/bin/activate  (ou venv\Scripts\activate sous Windows)
   pip install -r requirements.txt

3. Ajouter un fichier `secrets/config.yaml` contenant vos informations Azure

4. Lancer l’application :
   streamlit run app.py

## Technologies utilisées

- Streamlit pour l’interface
- LangChain pour l’indexation et le question-réponse
- LlamaIndex en alternative d’indexation
- Azure OpenAI pour les embeddings et le modèle de réponse
- PyMuPDF pour la lecture des fichiers PDF



