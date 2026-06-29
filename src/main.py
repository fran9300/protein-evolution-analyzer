from fastapi import FastAPI

from src.api.routes import router



app = FastAPI(

    title="Protein Evolution Analyzer",

    version="1.0"

)



app.include_router(

    router,

    prefix="/api"

)