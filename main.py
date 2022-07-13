import streamlit as st

from reader import *

st.set_page_config(
    page_title="BERT Keyword Extractor",
    page_icon="🎈",
)

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

reader = DocumentReader("rsvp-ai/bertserini-bert-base-squad")

def main():


    st.title("🔑 BERT Question Answerer")
    st.header("")

    with st.expander("ℹ️ - About this app", expanded=True):
        st.write(
            """     
    -   The *BERT Question Answerer* app is an easy-to-use interface built in Streamlit for the open-domain question answering system!
    -   It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to extract most common answer from the Internet .
    	    """
        )

        st.markdown("")

    st.markdown("")
    st.header("📌 Enter your question")

    with st.container():
        question = st.text_input("", "When was Barack Obama born?")

        answer = get_answer(question, reader)

        st.info(answer)


if __name__ == '__main__':
    main()
