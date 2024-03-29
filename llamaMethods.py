from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import PyPDF2
import pytesseract
from PIL import Image

MODEL_PATH = "./model/llama-2-7b-chat.Q8_0.gguf"
n_ctx = 2048

def getModel ():
    callbacks = CallbackManager ([StreamingStdOutCallbackHandler ()])
    model = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.5,
        n_gpu_layers=1000,
        max_tokens=1000,
        n_batch=4096,
        n_ctx=n_ctx,
        top_p=1,
        callback_manager=callbacks,
        verbose=True
    )

    return model

def getTextFromPDF (files):
    text = ""

    for file in files:
        if str (file.name).split (".")[-1] == "pdf":
            pdf_reader = PyPDF2.PdfReader (file)
            for page_num in range (len (pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text ()
            orgtext = " ".join (text.split ())
            text = orgtext
        elif (
            str (pdf_file.name).split (".")[-1] == "jpg"
            or str (pdf_file.name).split (".")[-1] == "jpeg"
            or str (pdf_file.name).split (".")[-1] == "png"
        ):
            photo = Image.open (file)
            docs = pytesseract.image_to_string (photo)
            text = docs

    return text

def loadModel (files, params):
    llm = getModel ()
    minLength = params["min"]
    maxLength = params["max"]

    template = """
        [INST] <<SYS>>
        You are tasked with summarizing the following text in a detailed manner within {min} to {max} words. Please ensure that your responses are socially unbiased and positive in nature.
        <</SYS>>
        {text}[/INST]
        """.strip()

    prompt = PromptTemplate (
        template=template,
        input_variables=["text", "min", "max"]
    )

    llm_chain = LLMChain (
        prompt=prompt,
        llm=llm
    )
    
    context_text = getTextFromPDF (files)
    model_responses = list ()
    if len (context_text) >= n_ctx:
        for i in range (0, len (context_text), n_ctx):
            model_responses.append (
                llm_chain.run (
                    text=context_text[i:i+n_ctx],
                    min=minLength - 30,
                    max=maxLength - 30
                )
            )

    return ''.join (model_responses)
