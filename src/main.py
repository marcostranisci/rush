import yaml
import os
from fastapi import FastAPI
from routers.query import query as query_router 
from internal.config import config as config
import uvicorn


app = FastAPI(
    title= f"API FastAPI rush",
    description="API FastAPI rush",
    version="0.1",
    openapi_tags=[
        {  
            "name": "rush",
        }
    ]
)

app.include_router(query_router)


@app.get("/")
async def root():
    return {"message": f"Benvenuto nell'API di {config.name}!"}



if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
