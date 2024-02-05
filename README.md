# Fastapi with MongoDB

A project to learn the mongo concepts. The project is a simple API to manage a list of costumers.

## Enviromments
To create a new enviroment
```python3 -m venv env```

To acivate the enviroment
```source env/bin/activate```

## How to run
To run the project, you need to have the python 3.8 installed. After that, you need to install the requirements with the command:
```pip install -r requirements.txt```

To run the project, you need to run the command:
```uvicorn app:app --reload```

The project will be running on the address: http://localhost:8000 by default.


## Features
- Create a new costumer
- List all costumers
- Get a costumer by id
- Update a costumer
- Delete a costumer

## How to use
- To create a new costumer, you need to make a POST request to the address: http://localhost:8000/costumers with the body:
```json
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "123456789",
    "city": "New York",
    "country": "USA",
    "active": True,
    "costumer_type": "Premium"
} 
```

- To list all costumers, you need to make a GET request to the address: http://localhost:8000/costumers

- To get a costumer by id, you need to make a GET request to the address: http://localhost:8000/costumers/{id}

- To update a costumer, you need to make a PUT request to the address: http://localhost:8000/costumers/{id} with the body:
```json
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "123456789",
    "city": "New York",
    "country": "USA",
    "active": True,
    "costumer_type": "Premium"
} 
```

- To delete a costumer, you need to make a DELETE request to the address: http://localhost:8000/costumers/{id}




## Requirements
- Python 3.8
- Fastapi
- Uvicorn
- PyMongo
