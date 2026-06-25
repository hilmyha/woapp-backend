from pydantic import BaseModel, EmailStr

class Category(BaseModel):
    name: str

class Exercise(BaseModel):
    name: str
    category_id: int

class ExerciseCreate(Exercise):
    pass

class ExerciseUpdate(BaseModel):
    name: str | None = None

class ExerciseResponse(Exercise):
    id: int
    category_id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }

class CategoryResponse(Category):
    id: int
    exercises: list[ExerciseResponse]

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }