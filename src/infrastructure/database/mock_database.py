from datetime import datetime
from typing import List, Optional
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class MockDatabase(UserRepository):
    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1
    
    def init_data(self):
        self._users = [
            User(id=1, name="Giovanni Martins", email="giovanni@giovanni.com", created_at=datetime.now()),
            User(id=2, name="Gio de Almeida", email="gio@gio.com", created_at=datetime.now()),
            User(id=3, name="giomartinsdev", email="giomartinsdev@gio.com", created_at=datetime.now()),
        ]
        self._next_id = len(self._users) + 1
    
    def create(self, user: User) -> User:
        self._users.append(user)
        return user
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def get_all(self) -> List[User]:
        return self._users.copy()
    
    def update(self, user: User) -> User:
        for i, existing_user in enumerate(self._users):
            if existing_user.id == user.id:
                self._users[i] = user
                return user
        raise ValueError(f"Usuário com ID {user.id} não encontrado")
    
    def delete(self, user_id: int) -> bool:
        for i, user in enumerate(self._users):
            if user.id == user_id:
                del self._users[i]
                return True
        return False
