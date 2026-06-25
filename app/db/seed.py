from sqlalchemy.orm import Session
from app.modules.exercises.exercise_model import CategoryModel, ExerciseModel


def seed_categories(db: Session):
    categories = [
        "Chest",
        "Back",
        "Legs",
        "Shoulders",
        "Arms",
        "Core",
        "Cardio",
    ]

    existing = {c.name for c in db.query(CategoryModel).all()}

    for name in categories:
        if name not in existing:
            db.add(CategoryModel(name=name))

    db.commit()


def seed_exercises(db: Session):
    categories = db.query(CategoryModel).all()

    category_map = {c.name: c for c in categories}

    exercises_data = [
        ("Bench Press", "Chest"),
        ("Incline Press", "Chest"),
        ("Chest Fly", "Chest"),

        ("Lat Pulldown", "Back"),
        ("Seated Row", "Back"),
        ("Barbell Row", "Back"),

        ("Squat", "Legs"),
        ("Leg Press", "Legs"),
        ("Leg Curl", "Legs"),

        ("Shoulder Press", "Shoulders"),
        ("Lateral Raise", "Shoulders"),

        ("Barbell Curl", "Arms"),
        ("Hammer Curl", "Arms"),
        ("Tricep Pushdown", "Arms"),

        ("Plank", "Core"),
        ("Crunch", "Core"),

        ("Treadmill", "Cardio"),
        ("Cycling", "Cardio"),
    ]

    existing = {e.name for e in db.query(ExerciseModel).all()}

    for name, category_name in exercises_data:
        if name in existing:
            continue

        category = category_map.get(category_name) # type: ignore
        if not category:
            continue

        db.add(ExerciseModel(
            name=name,
            category_id=category.id
        ))

    db.commit()