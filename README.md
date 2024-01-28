# PDF Summarizer

PDF Summarizer is an application that leverages the power of the LLAMA model to summarize PDF documents. The LLAMA model, which can be downloaded from [this link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main), provides advanced natural language processing capabilities for generating concise and informative summaries.

## Features

- Summarize PDF documents using state-of-the-art language model (LLAMA).
- Streamlit is employed for a user-friendly and interactive interface.
- Easy-to-use and efficient summarization process.

## Getting Started

Follow these steps to set up and run the PDF Summarizer:

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Download the LLAMA model from [this link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main) and save it in the `models` directory.

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Access the application in your web browser at `http://localhost:8501`.

## Usage

1. Upload a PDF document using the provided interface.
2. Click the "Summarize" button to initiate the summarization process.
3. View and download the generated summary.

## Dependencies

- Python 3.x
- Streamlit

## Acknowledgments

- [LLAMA Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main) by TheBloke.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
