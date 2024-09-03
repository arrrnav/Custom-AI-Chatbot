from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from langchain_openai import OpenAI
import pdfplumber
from getpass import getpass
import os

# Set the OpenAI API Key
# WARNING: YOUR INPUT WILL BE HIDDEN, BUT IT IS STILL BEING ENTERED #
os.environ["OPENAI_API_KEY"] = getpass("Enter OpenAI API Key here: ")

def generate_text_file(pdf_directory_path):
    text = ''
    with pdfplumber.open(pdf_directory_path) as pdf:
        for page in pdf.pages:
            # Extract text // x_tolerance used to make sure pdfplumber can distinguish spaces between words
            page_text = page.extract_text(x_tolerance=1)
            
            # Extract images
            images = page.images
            
            # Append filtered text to result
            text += page_text + '\n'
    return text
    
# outstream = open(INSERT PATH TO TXT FILE TO WRITE TO HERE, "w", encoding='utf-8')
# outstream.write(generate_text_file(INSERT PATH TO PDF TO CONVERT HERE))
# outstream.close()


def construct_index(text_directory_path):
    # define LLM
    Settings.llm = OpenAI(temperature=0.5, model_name="gpt-4o", max_tokens=2000)
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    Settings.num_output = 2000
    Settings.context_window = 4096
 
    documents = SimpleDirectoryReader(text_directory_path).load_data()
    
    index = VectorStoreIndex.from_documents(documents)

    try:  
        os.mkdir("./storage")  
    except FileExistsError as error:
        pass

    index.storage_context.persist(persist_dir="./storage")
    return index

# construct_index(INSERT PATH TO FOLDER CONTAINING TXT FILES TO INDEX HERE)