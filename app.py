from flask import Flask
from src.presentation.controllers.user_controller import user_bp
from src.infrastructure.spec.spec_tree import api
from src.infrastructure.database.mock_database import MockDatabase
from src.application.services.user_service import UserService
from src.infrastructure.dependency_container import container
from src.presentation.middleware.exception_handler import handle_exceptions

app = Flask(__name__)

# Configurar middleware de exceções
handle_exceptions(app)

db = MockDatabase()
db.init_data()
container.set('user_repository', db)
container.set('user_service', UserService(db))

app.register_blueprint(user_bp)
api.register(app)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
