# Python Training API

Welcome to my Python Training API ! This API is built using FastAPI and is designed to interact with a PostgreSQL database through SQLAlchemy. It leverages Pydantic for data validation and serialization.

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn (ASGI server)
- PostgreSQL

## Setup

#### Clone the repository : 
```bash
git clone https://github.com/Quentiinos/API.git
```

#### Install dependencies :

```bash
pip install fastapi sqlalchemy pydantic psycopg2-binary uvicorn python-dotenv
```

## Configuation

Set up your PostgreSQL database and update the database URL in your configuration file ( **.env** ).  

The URL format is :
```bash
postgresql://user:password@server/database
```

## Usage

#### Start the server :
```bash
uvicorn app.main:app --reload
```

#### Access the API documentation at :
    
- **Swagger UI :** http://127.0.0.1:8000/docs
- **ReDoc :** http://127.0.0.1:8000/redoc

## Support

For support, please contact [@Quentiinos](https://github.com/quentiinos).