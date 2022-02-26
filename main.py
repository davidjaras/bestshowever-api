import os

import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse

from functions import create_zip, get_endpoint

app = FastAPI()


@app.get("/thebestshowevercharacters/")
def the_best_show_ever_characters(
    name: str = None, status: str = None, gender: str = None, download: bool = False
):

    endpoint = f"https://rickandmortyapi.com/api/character/?"
    endpoint = get_endpoint(endpoint, name, status, gender)

    response = requests.get(endpoint)

    if download:
        file_path = create_zip(response.json())
        if os.path.exists(file_path):
            return FileResponse(file_path, filename="response.zip")

    return response.json()


@app.get("/whoisid/{id}")
def who_is_id(id):
    endpoint = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(endpoint)
    return response.json().get("name")
