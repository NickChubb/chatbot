# LlamaIndex RAG

https://docs.llamaindex.ai/en/stable/index.html

## Errors

```
ValueError: No API key found for OpenAI.
Please set either the OPENAI_API_KEY environment variable or openai.api_key prior to initialization.
API keys can be found or created at https://platform.openai.com/account/api-keys
```

fix: https://stackoverflow.com/questions/76771761/why-does-llama-index-still-require-an-openai-key-when-using-hugging-face-local-e

```
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
INFO:openai._base_client:Retrying request to /embeddings in 6.511309 seconds
Retrying request to /embeddings in 6.511309 seconds
```

fix: 