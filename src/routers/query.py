import requests
from fastapi import FastAPI, HTTPException, Query, APIRouter
from SPARQLWrapper import SPARQLWrapper, JSON
import yaml
import os,json
from internal.schemas import ExtractedKnowledge,UncertaintyList
from internal.config import config as config 
from scripts.retrieval import Retriever
from scripts.translate import Translator

retriever = Retriever()
translator = Translator()

query = APIRouter(
    prefix="/query",
    tags=["query"],
    responses={404: {"description": "Not found"}},
)


@query.get("/graphrag",response_model=ExtractedKnowledge)
def retrieve(text:str):
    
    res = retriever.extract_knowledge(text=text)
    res = json.loads(res)

    my_res = dict()

    my_res['template'] = res

    return my_res

@query.get("/translate",response_model=UncertaintyList)

def translate(text:str,lang:str):

    translated = translator.translate(text,lang)
    
    return translated