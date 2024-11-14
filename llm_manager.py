from transformers import AutoTokenizer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings

class LLMManager:

    def __init__(self,
                 model_id ="meta-llama/Llama-3.2-1B-instruct",
                 model_embedding = "BAAI/bge-m3",                 
                ):
        # Create the model, embedding, and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.llm = HuggingFaceLLM(model_name=model_id, tokenizer=self.tokenizer)
        self.embed_model = HuggingFaceEmbedding(model_name=model_embedding)

        # LlamaIndex Setup
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        Settings.chunk_size = 1024

        print(f"LLM Initailized.")