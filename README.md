# rush

This repo is a fast api service that supports:

* the translation from English to Arabic and viceversa.
* the extraction of structured knowledge from raw text

## How to

1. build the docker file

> docker build -t rush-api .

2. docker run -p 8000:8000 rush-api

3. API playground is then available at 0.0.0.0/8000/docs

### Translate

Endpoint
> 0.0.0.0/800/query/translate

**parameters**
> text: str # the text to be translated
> lang: str (en o ar) # the language of the text that must be translated

**output**

a dictionary with two fields

* uncertainty: a list of translated and their uncertainty scores
* translated: the full translation

### Extract

This is an alpha version of the Knowledge Extractor. It doesn't work but it gives insights about model dimensionality and computational requirements in a small-scaled setting.

Endpoint
> 0.0.0.0/800/query/translate


**parameters**
> text: str # the text from which the knowledge must be extracted (language agnostic)

**output**

a dictionary with all the extracted entities
