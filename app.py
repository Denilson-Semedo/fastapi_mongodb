from fastapi import FastAPI, HTTPException
from config.database import client
from models.costumers import Costumer
from typing import List

app = FastAPI(title="MongoDB FastAPI Integration", description="A simple example showing how to integrate MongoDB with FastAPI", version="0.0.1")

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


@app.post("/costumer")
def create_costumer(costumer: Costumer):
    # Create a new costumer
    try:
        db = client.test
        collection = db.costumers
        result = collection.insert_one(costumer.dict())
        return {"message": "Costumer created successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/costumer/{id}")
def get_costumer(id: str) -> Costumer:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find_one({"_id": id})
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/costumers")
def get_costumers() -> List[Costumer]:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))