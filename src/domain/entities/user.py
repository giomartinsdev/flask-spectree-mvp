from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.domain.exceptions.domain_exceptions import RequiredFieldError, InvalidEmailError


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        self.validate()
    
    def validate(self):
        if not self.name or not self.name.strip():
            raise RequiredFieldError("Nome é obrigatório")
        
        if not self.email or "@" not in self.email:
            raise InvalidEmailError("Email inválido")
    
    def update(self, name: Optional[str] = None, email: Optional[str] = None):
        if name:
            self.name = name
        if email:
            self.email = email
        self.validate()
        self.updated_at = datetime.now()
