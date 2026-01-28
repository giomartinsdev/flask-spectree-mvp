from flask import jsonify
from src.domain.exceptions.domain_exceptions import (
    ValidationError, 
    NotFoundError, 
    UserNotFoundError, 
    UserCreationError,
    DomainException
)


def handle_exceptions(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "Validation Error",
            "message": str(error)
        }), 400
    
    @app.errorhandler(UserNotFoundError)
    def handle_user_not_found_error(error):
        return jsonify({
            "error": "Not Found", 
            "message": str(error)
        }), 404
    
    @app.errorhandler(NotFoundError)
    def handle_not_found_error(error):
        return jsonify({
            "error": "Not Found",
            "message": str(error)
        }), 404
    
    @app.errorhandler(UserCreationError)
    def handle_user_creation_error(error):
        return jsonify({
            "error": "Creation Error",
            "message": str(error)
        }), 400
    
    @app.errorhandler(DomainException)
    def handle_domain_error(error):
        return jsonify({
            "error": "Domain Error",
            "message": str(error)
        }), 400
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }), 500
