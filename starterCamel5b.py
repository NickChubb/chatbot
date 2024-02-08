# reference: https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel.html
# currently working but extremely slow

import logging
import sys
import os.path

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from llama_index.llms import HuggingFaceLLM
# setup prompts - specific to StableLM
from llama_index.prompts import PromptTemplate

# This will wrap the default prompts that are internal to llama-index
# taken from https://huggingface.co/Writer/camel-5b-hf
query_wrapper_prompt = PromptTemplate(
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n{query_str}\n\n### Response:"
)

# Define LLM model
llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=256,
    # temperature regulates the randomness, or creativity, of the AI’s responses.
    # A higher temperature value typically makes the output more diverse and creative 
    # but might also increase its likelihood of straying from the context. 
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="Writer/camel-5b-hf",
    model_name="Writer/camel-5b-hf",
    device_map="auto",
    tokenizer_kwargs={"max_length": 2048},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
    model_kwargs={"offload_folder": "offload"}
)

service_context = ServiceContext.from_defaults(chunk_size=512, llm=llm, embed_model="local")

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents, service_context=service_context, show_progess=True)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine(logging="DEBUG")
response = query_engine.query("What did the author do growing up?")
print(response)