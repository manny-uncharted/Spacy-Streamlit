# Core Packages
import streamlit as st



# NLP Packages
import spacy_streamlit
import en_core_web_sm
import spacy

# Create NLP object
nlp = spacy.load("en_core_web_sm")

# Main app
def main():
    """A simple NLP app with Spacy-streamlit"""

    st.title("NLP App with Spacy-Streamlit")

    menu = ["Home", "NER", "Categories"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.spinner("Loading Home ..."):
            st.markdown("""
            This is a simple NLP app with Spacy-Streamlit.
            """)
            st.success("Done!")
        st.subheader("Tokenization")
        raw_text = st.text_area("Your Text", "Type Here")
        document = nlp(raw_text)
        if st.button("Tokenize"):
            spacy_streamlit.visualize_tokens(document, attrs=['text', 'pos_', 'dep_', 'ent_type_', 'lemma_'])
    elif choice == "NER":
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Your Text", "Type Here")
        document = nlp(raw_text)
        spacy_streamlit.visualize_ner(document, labels=nlp.get_pipe('ner').labels)
    elif choice == "Categories":
        st.subheader("Categories of Words according to Parse Of Sentence")
        raw_text = st.text_area("Your Text", "Type Here")
        document = nlp(raw_text)
        spacy_streamlit.visualize_parser(document)



if __name__ == "__main__":
    main()