def costumers_serializer(costumer) -> dict:
    return {
        "id": str(costumer["_id"]),
        "name": costumer["name"],
        "email": costumer["email"],
        "phone": costumer["phone"],
        "city": costumer["city"],
        "country": costumer["country"],
        "created_at": costumer["created_at"],
        "updated_at": costumer["updated_at"],
        "deleted_at": costumer["deleted_at"],
        "active": costumer["active"],
        "costumer_type": costumer["costumer_type"]
    }


def costumers_serializer_list(costumers) -> list:
    return [costumers_serializer(costumer) for costumer in costumers]