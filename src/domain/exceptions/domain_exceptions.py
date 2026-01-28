class DomainException(Exception):
    """Base exception for domain errors"""
    pass


class ValidationError(DomainException):
    """Raised when validation fails"""
    pass


class NotFoundError(DomainException):
    """Raised when a resource is not found"""
    pass


class InvalidEmailError(ValidationError):
    """Raised when email is invalid"""
    pass


class RequiredFieldError(ValidationError):
    """Raised when a required field is missing or empty"""
    pass


class UserNotFoundError(NotFoundError):
    """Raised when user is not found"""
    pass


class UserCreationError(DomainException):
    """Raised when user creation fails"""
    pass
