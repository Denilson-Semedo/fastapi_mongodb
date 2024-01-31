import datetime
from fastapi import APIRouter, HTTPException
from config.database import client
from modules.costumers.models.costumers import Costumer, CostumerReturn, CostumerUpdate
from typing import List
from bson.objectid import ObjectId

router = APIRouter(tags=["Costumers"], prefix="/costumers", responses={404: {"description": "Not found"}}, )

@router.post("/costumer")
async def create_costumer(costumer: Costumer):
    # Create a new costumer
    try:
        db = client.test
        collection = db.costumers
        result = collection.insert_one(costumer.dict())
        return {"message": "Costumer created successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/costumer/{id}")
async def get_costumer(id: str) -> CostumerReturn:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find_one({"_id": id})
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/costumers")
async def get_costumers() -> List[CostumerReturn]:
    try:
        db = client.test
        collection = db.costumers
        result = collection.find()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.put("/costumer/{id}")
async def update_costumer(id: str, costumer: CostumerUpdate):
    
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    costumer.update({
        "updated_at": updated_at
    })
    
    try:
        db = client.test
        collection = db.costumers
        result = collection.update_one({"_id": id}, {"$set": costumer.dict()})
        return {"message": "Costumer updated successfully", "id": id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/costumer/{id}")
async def delete_costumer(id: str):
    try:
        db = client.test
        collection = db.costumers
        result = collection.delete_one({"_id": id})
        return {"message": "Costumer deleted successfully", "id": id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))