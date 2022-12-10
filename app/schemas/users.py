def UsersEntity(item) -> dict:
    return {
            "id": item ["id"],
            "name": item ["name"],
            "email": item ["email"],
            "password": item ["password"]
    }
def UserEntity(entity) -> list:
        [UserEntity(item) for item in entity]
