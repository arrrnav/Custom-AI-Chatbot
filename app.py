from flask import Flask, render_template, request
from llama_index.core import StorageContext, load_index_from_storage
from getpass import getpass
import os

# Set the OpenAI API Key
os.environ["OPENAI_API_KEY"] = "INSERT OPENAI KEY HERE"
app = Flask(__name__)
llm_index = load_index_from_storage(StorageContext.from_defaults(persist_dir="./storage"))

def ask_ai(query: str):
    query_engine = llm_index.as_query_engine()
    response = query_engine.query(query)
    return str(response)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_chat_response(input)

# TESTING IMPLEMENTATION
#   chatbot will reply with ai replies
def get_chat_response(query):
    # return query
    return ask_ai(query)

if __name__ == '__main__':
    app.run(debug=True)