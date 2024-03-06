from fastapi import FastAPI
from uvicorn import run
from api import v1Router


# FastAPI setup
app = FastAPI(title='Simple Test FastAPI Server',openapi_url="/openapi.json", docs_url="/docs")
app.include_router(v1Router, prefix="/api")



if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port=8001, reload=True)