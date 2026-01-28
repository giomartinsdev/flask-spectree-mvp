from typing import List, Optional
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.domain_exceptions import UserNotFoundError, UserCreationError


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def create_user(self, name: str, email: str) -> User:
        try:
            existing_users = self.user_repository.get_all()
            new_id = max([user.id for user in existing_users], default=0) + 1
            
            user = User(id=new_id, name=name, email=email)
            return self.user_repository.create(user)
        except Exception as e:
            raise UserCreationError(f"Failed to create user: {str(e)}")
    
    def get_user(self, user_id: int) -> User:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")
        return user
    
    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all()
    
    def update_user(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> User:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")
        
        user.update(name=name, email=email)
        return self.user_repository.update(user)
    
    def delete_user(self, user_id: int) -> bool:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"User {user_id} not found")
        
        return self.user_repository.delete(user_id)
