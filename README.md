# Spacy-Streamlit

Here is using a library by explosion ai labs to build a simple app that takes sentences and tokenizes them generating their part of speech, word forms, lemmas and name-entities. 

It uses spacy to build the model and streamlit to deploy the app.

## Installation
- Create a virtual environment and run the following commands
    ```bash
    pip install -r requirements.txt
    ```
    and also download the spacy model for the English language, with your command line in administrator mode.
    
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage
- Run the following command in your command line
    ```bash
    streamlit run app.py
    ```

## About the App
- The app is a simple web app that takes a sentence as input and tokenizes it, generating the part of speech, word forms, lemmas and name-entities of the sentence. It can also be used to generate the dependency parse of the sentence.
