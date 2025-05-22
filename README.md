## API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI. Once your server is running, you can access the OpenAPI docs at:

```
http://127.0.0.1:8000/docs
```

You can also access the alternative ReDoc documentation at:

```
http://127.0.0.1:8000/redoc
```
## FastAPI Project Setup

### 1. Set up a virtual environment

```bash
python3 -m venv .venv
```

### 2. Install FastAPI and Uvicorn

```bash
pip install fastapi
pip install uvicorn
```

*`uvicorn` is a server used to run and test your FastAPI application.*

### 3. Run the FastAPI application

```bash
uvicorn main:app --reload
```

*This command starts the FastAPI app defined in `main.py` with auto-reload enabled for development.*