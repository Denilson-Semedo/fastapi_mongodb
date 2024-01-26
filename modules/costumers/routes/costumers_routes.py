from fastapi import APIRouter, HTTPException
from config.database import client
from modules.costumers.models.costumers import Costumer
from typing import List

router = APIRouter(tags=["Costumers"], prefix="/costumers")

@router.post("/costumer")
def create_costumer(costumer: Costumer):
    # Create a new costumer
    try:
        db = client.test
        collection = db.costumers
        result = collection.insert_one(costumer.dict())
        return {"message": "Costumer created successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/costumer/{id}")
def get_costumer(id: str) -> Costumer:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find_one({"_id": id})
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/costumers")
def get_costumers() -> List[Costumer]:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))