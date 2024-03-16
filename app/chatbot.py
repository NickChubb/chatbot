import os
from llama_index.llms.openai import OpenAI
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
    load_index_from_storage
)

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if OPENAI_API_KEY is None:
    secret_file_path = '/run/secrets/OPENAI_API_KEY'
    
    if os.path.isfile(secret_file_path):
        with open(secret_file_path, 'r') as secret_file:
            OPENAI_API_KEY = secret_file.read().strip()
            os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Set the LLM to ChatGPT-4
llm = OpenAI(temperature=1, model="gpt-3.5-turbo")

# check if storage already exists
PERSIST_DIR = "./storage-gpt4"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context, llm=llm)

def query(query):
    query_wrapper = "You are Nick Chubb, from the provided data only. \
        Respond naturally in first person, like a human would respond in a job interview. \
        Your knowledge is limited to the information provided to you, feel free to elaborate a little. \
        Respond to the following query with 3 - 4 lines only: "
    chat_engine = index.as_chat_engine()
    response = chat_engine.chat(query_wrapper + query)
    return str(response)

def generate(query):
    # query_wrapper = "Using only the provided context, you are to return an\
    #     valid block of HTML code which builds a page based on the input context.\
    #     Use data from the context to fill information about the topic. Include style tags \
    #     and centering divs to make the page look nice. Make sure the colors of the text and the background do \
    #     not overlap significatnly. Make it as fun and interactive as possible, using javascript and jquery. \
    #     Here is the topic and specifications for the html component you should generate, based on the given context: "
    query_wrapper = ""
    query_engine = index.as_query_engine(llm=llm)
    response = query_engine.query(query_wrapper + query)
    return str(response)