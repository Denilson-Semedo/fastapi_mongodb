from pydantic import BaseModel

class Costumer(BaseModel):
    name: str
    email: str
    phone: str
    city: str
    country: str
    created_at: str
    updated_at: str
    deleted_at: str
    active: bool
    costumer_type: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "name": "John Doe",
                "email": "john@email.com",
                "phone": "123456789",
                "city": "New York",
                "country": "USA",
                "created_at": "2021-01-01 00:00:00",
                "updated_at": "2021-01-01 00:00:00",
                "deleted_at": "2021-01-01 00:00:00",
                "active": True,
                "costumer_type": "Premium"
            }
            ]
        }
    }

    
    
    