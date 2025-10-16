from transformers import AutoModelForCausalLM, AutoTokenizer
import torch,json
from sentence_transformers import SentenceTransformer
import json
from internal.config import config

sentence_model = SentenceTransformer("all-MiniLM-L6-v2")



class Retriever:
    def __init__(self):
        self.model_name = "numind/NuExtract-tiny-v1.5"
        self.device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name, torch_dtype=torch.bfloat16, trust_remote_code=True).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)


    def extract_knowledge(self, text, template=config.template, max_length=10_000, max_new_tokens=4_000):
        model = self.model
        tokenizer = self.tokenizer
        
        prompt = f"""<|input|>\n### Template:\n{template}\n### Text:\n{text}\n\n<|output|>"""
        outputs = []
        with torch.no_grad():
            
            batch_encodings = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=max_length).to(model.device)
            pred_ids = model.generate(**batch_encodings, max_new_tokens=max_new_tokens)
            outputs += tokenizer.batch_decode(pred_ids, skip_special_tokens=True)
            
        print(outputs[0].split("<|output|>")[1])
        return outputs[0].split("<|output|>")[1]
    
