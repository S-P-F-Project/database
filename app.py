import contextlib

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/ping")
async def pong():
    return PlainTextResponse("ok", 200)


# app.include_router(router)
