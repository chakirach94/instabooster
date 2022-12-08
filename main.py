
from typing import Union
from fastapi import FastAPI
import requests
import json
from fastapi.responses import RedirectResponse, HTMLResponse
import random

app = FastAPI()

def srachuser(myuser):
  url = "https://instagram-scraper-2022.p.rapidapi.com/ig/info_username/"
  querystring = {"user":myuser}
  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response.text)
  return jess_dict2



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/finduser/{item_id}")
async def finduser(item_id: str, q: Union[str, None] = None):
    link=srachuser(item_id)
    return link
