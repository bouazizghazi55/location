# -*- coding: utf-8 -*-
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
"""
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Data(BaseModel):
    name: str
    job:str
    
    #observations: str
    #location_data: list

app = FastAPI()


@app.post("/data/")
async def create_data(data: Data):
    return data
    