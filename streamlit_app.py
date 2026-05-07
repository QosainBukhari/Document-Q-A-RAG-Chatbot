import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="RAG Chatbot",
    layout="wide"
)

st.title("📄 Document Q&A RAG Chatbot")


# Upload section
st.header("Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    if st.button("Upload PDF"):

        with st.spinner("Uploading and processing PDF..."):

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

            result = response.json()

            if "error" in result:

                st.error(result["error"])

            else:

                st.success(result["message"])

                st.write(
                    f"Chunks created: {result['total_chunks']}"
                )


# Chat section
st.header("Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Generating answer..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": question
                }
            )

            result = response.json()

            if "error" in result:

                st.error(result["error"])

            else:

                st.subheader("Answer")

                st.write(result["answer"])

                st.subheader("Sources")

                for source in result["sources"]:

                    st.write(source)

    else:

        st.warning("Please enter a question.")