# Flask Spectree MVP

Minimal Flask application demonstrating Spectree for automatic OpenAPI documentation.

## Overview

This MVP shows Spectree integration with:
- **Spectree** for automatic OpenAPI 3.0 documentation
- **Pydantic** for request/response validation
- **Flask** web framework

## Quick Start

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5001/doc/swagger` for interactive documentation in swagger and `http://localhost:5001/doc/openapi.json` for the OpenAPI specification.

## Spectree Configuration

```python
from spectree import SpecTree

api = SpecTree(
    'flask',
    path='doc',        # Documentation endpoint
    mode='strict'      # Strict validation mode
)
```

## Usage Example

```python
@user_bp.route('', methods=['POST'])
@api.validate(
    json=UserCreateRequest,
    resp=Response(HTTP_201=UserResponse, HTTP_400=ErrorResponse),
    tags=['Users']
)
def create_user(json: UserCreateRequest):
    # Handler logic
    pass
```

## Dependencies

- **Flask 3.0.0**
- **Spectree 2.0.1**
- **Pydantic 2.11**
