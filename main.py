
from typing import Union
from fastapi import FastAPI
import requests
import json
from fastapi.responses import RedirectResponse, HTMLResponse
import random

app = FastAPI()

def channelsearch(channel):
  url = "https://youtube-media-downloader.p.rapidapi.com/v2/search/channels"

  querystring = {"keyword":channel,"sortBy":"relevance"}

  headers = {
    "X-RapidAPI-Key": "68a49ac1a2msh3a7b4896a584357p137023jsn9db99d40833e",
    "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  jess_dict2 = json.loads(response.text)
  if jess_dict2['status']==True:
      return jess_dict2
  return "false"



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get/profil/{item_id}")
def searsh(item_id: str, q: Union[str, None] = None):
        
        return {"results":{item_id} }
