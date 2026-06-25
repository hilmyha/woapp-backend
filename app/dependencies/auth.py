from typing import Annotated
from fastapi import Depends

from app.middleware.auth import get_current_user
from app.modules.users.user_model import UserModel

CurrentUser = Annotated[
    UserModel,
    Depends(get_current_user)
]