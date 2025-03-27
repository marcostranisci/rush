from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch,json,sentencepiece


class Translator:
    def __init__(self):
        self.ar_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ar-en",torch_dtype=torch.bfloat16).eval()
        self.ar_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ar-en")
        self.en_ar = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ar",torch_dtype=torch.bfloat16).eval()
        self.en_ar_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
        self.loss = torch.nn.CrossEntropyLoss()
    
    def translate(self,text,lang):
        if lang == 'ar':
            input_ids = self.ar_en_tokenizer.encode(text, return_tensors="pt", padding=True)
            outputs = self.ar_en.generate(input_ids,output_scores=True, return_dict_in_generate=True)
        
        
            uncertainty = list()
            for i in range(1, len(outputs.scores)):
                scores = outputs.scores[i][0]
                token = self.ar_en_tokenizer.decode(torch.argmax(scores))
                loss = self.loss(scores,torch.argmax(scores))
                uncertainty.append({'token':token,'loss':loss.item()})
            decoded = self.ar_en_tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)

            results = {'uncertainty':uncertainty,'translated':decoded}
            return results
        elif lang == 'en': 
            input_ids = self.en_ar_tokenizer.encode(text, return_tensors="pt", padding=True)
            outputs = self.en_ar.generate(input_ids,output_scores=True, return_dict_in_generate=True)
        
        
            uncertainty = list()
            for i in range(1, len(outputs.scores)):
                scores = outputs.scores[i][0]
                token = self.en_ar_tokenizer.decode(torch.argmax(scores))
                loss = self.loss(scores,torch.argmax(scores))
                uncertainty.append({'token':token,'loss':loss.item()})
            decoded = self.en_ar_tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)

            results = {'uncertainty':uncertainty,'translated':decoded}
            return results
