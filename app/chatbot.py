import os
# Set to llama_index.core when running locally
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if OPENAI_API_KEY is None:
    secret_file_path = '/run/secrets/OPENAI_API_KEY'
    
    if os.path.isfile(secret_file_path):
        with open(secret_file_path, 'r') as secret_file:
            OPENAI_API_KEY = secret_file.read().strip()
            os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

def query(message):
    query_engine = index.as_chat_engine()
    response = query_engine.chat(message)
    return str(response)

