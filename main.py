import streamlit as stm
from llamaMethods import loadModel

if __name__ == "__main__":
    stm.title("PDF Summarizer")

    with stm.sidebar:
        stm.header("Options")
        files = stm.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)

        stm.header("Summarized Length")
        length = stm.radio("Select the length of the summary", ["Short", "Medium", "Long"], index=1)
        if length == "Short":
            params = { "min": 20, "max": 50 }
        elif length == "Medium":
            params = { "min": 50, "max": 100 }
        elif length == "Long":
            params = { "min": 100, "max": 200 }

    if files is not None:
        if stm.button("Summarize"):
            response = loadModel(files, params)
            stm.write(response)
