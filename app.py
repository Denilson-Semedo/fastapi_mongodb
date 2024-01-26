from fastapi import FastAPI, HTTPException
from config.database import client

from modules.costumers.routes.costumers_routes import router as costumers_router

app = FastAPI(title="MongoDB FastAPI Integration", description="A simple example showing how to integrate MongoDB with FastAPI", version="0.0.1")

app.include_router(costumers_router)

@app.get("/")
def read_root():
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        return {"message": "Successfully connected to MongoDB"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@app.get("/databases")
def get_databases():
        
        # List all databases on the server
        try:
            return {"databases": client.list_database_names()}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        