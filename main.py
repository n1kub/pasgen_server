import logging
import webbrowser
from logging.config import dictConfig

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from my_logger import LogConfig
from service.api_models.password_req import PasswordRequest
from service.password_generation import generate_new_password, update_password
import web

app = FastAPI(debug=True)

dictConfig(LogConfig().dict())
logger = logging.getLogger("mylogger")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(packages=[("web", '')], html=True), name="web")


@app.post("/password")
async def root(pass_req: PasswordRequest):
    if len(pass_req.password_to_modify) == 0:
        logger.info(f'New request to generate password with length {pass_req.password_length}')
        return generate_new_password(pass_req.password_length, pass_req.has_upper, pass_req.with_special_symbols)
    else:
        logger.info(f'New request to modify password: {pass_req.password_to_modify}')
        return update_password(pass_req.password_to_modify, pass_req.has_upper, pass_req.with_special_symbols)


if __name__ == "__main__":
    webbrowser.open("http://localhost:8080/")
    uvicorn.run(app, host="127.0.0.1", port=8080)
