from fastapi import FastAPI
from pyenigma_api.main import enigma
from json import dumps

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is the root for APIs in enigma"}


@app.get("/plugboard/shorts")
async def get_plugboard_shorts():
    return {"shorts_list": enigma.switchboard_shorts}