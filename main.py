import streamlit as stm
from llamaMethods import loadModel

if __name__ == "__main__":
    stm.title("PDF Summarizer")
    
    with stm.sidebar:
        stm.header("Options")
        file = stm.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)
        
        # three options describing the summarized length of the output
        # short, medium, long
        # short: 20-50 words
        # medium: 50-100 words
        # long: 100-200 words
        # default: medium
    
        stm.header("Summarized Length")
        length = stm.radio("Select the length of the summary", ["Short", "Medium", "Long"], index=1)
        if length == "Short":
            params = { "min": 20, "max": 50 }
        elif length == "Medium":
            params = { "min": 50, "max": 100 }
        elif length == "Long":
            params = { "min": 100, "max": 200 }
        
    if file is not None:
        if stm.button("Summarize"):
            for chunk in file:
                summary = loadModel (chunk, params)
                stm.write(summary)