# API Flask com DDD e Spectree

API simples implementada com Flask, Domain-Driven Design (DDD) e Spectree para geração automática de documentação Swagger.

## Estrutura do Projeto

```
src/
├── domain/
│   ├── entities/          # Entidades de domínio
│   ├── repositories/      # Interfaces de repositórios
│   └── services/          # Serviços de domínio
├── infrastructure/
│   └── database/          # Implementação de repositórios (Mock)
└── presentation/
    ├── controllers/       # Controllers/Endpoints
    └── dtos/             # Data Transfer Objects
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## Endpoints

### Usuários

- `GET /api/users` - Listar todos os usuários
- `GET /api/users/{id}` - Buscar usuário por ID
- `POST /api/users` - Criar novo usuário
- `PUT /api/users/{id}` - Atualizar usuário
- `DELETE /api/users/{id}` - Deletar usuário

## Documentação Swagger

Acesse `http://localhost:5000/doc` para ver a documentação interativa gerada pelo Spectree.

## Exemplos de Uso

### Criar Usuário
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Novo Usuário", "email": "novo@example.com"}'
```

### Listar Usuários
```bash
curl http://localhost:5000/api/users
```

### Buscar Usuário
```bash
curl http://localhost:5000/api/users/1
```

### Atualizar Usuário
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Nome Atualizado"}'
```

### Deletar Usuário
```bash
curl -X DELETE http://localhost:5000/api/users/1
```
