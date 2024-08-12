from fastapi import FastAPI
from typing import Tuple, List, Dict
from pyenigma_api.plugboard import PlugBoard
from json import dumps

app = FastAPI()
plugboard = PlugBoard()

@app.get("/")
async def root():
    return {"message": "This is the root for APIs in enigma"}


@app.get("/plugboard/shorts")
async def get_all_plugboard_shorts()-> Dict[str, List[Tuple[int, int]]]:
    """Gets all the shorts in the plugboard"""
    return {"shorts_list": plugboard.shorts}

@app.post("/plugboard/add_short", status_code= 201)
async def add_short(short: Tuple[int, int]):
    
    try:
        plugboard.add_short(short)
        return {"status": "success", "short_added": short}
    except Exception as e:
        return {"status": "failure", "reason":str(e)}

@app.post("/plugboard/add_shorts", status_code= 201)
async def add_shorts(shorts_list: List[Tuple[int, int]]):
    add_success_list = []
    add_failure_list = []
    for short in shorts_list:
        try:
            plugboard.add_short(short)
            add_success_list.append(short)
        except Exception as e:
            add_failure_list.append({"failed_short":short, "reason": str(e)})
    
    return {"success_list": add_success_list, "failed_list": add_failure_list}
    
@app.post("/plugboard/remove_short", status_code= 201)
async def remove_short(short: Tuple[int, int]):
    try:
        plugboard.remove_short(short)
        return {"status": "success", "short_removed": short}
    except Exception as e:
        return {"status": "failure", "reason":str(e)}
    
@app.post("/plugboard/remove_shorts", status_code= 201)
async def add_shorts(shorts_list: List[Tuple[int, int]]):
    remove_success_list = []
    remove_failure_list = []
    for short in shorts_list:
        try:
            plugboard.add_short(short)
            remove_success_list.append(short)
        except Exception as e:
            remove_failure_list.append({"failed_short":short, "reason": str(e)})
    
    return {"success_list": remove_success_list, "failed_list": remove_failure_list}
    
@app.post("/plugboard/get_ouput", status_code= 201)
async def get_output(input_int: int):
    try:
        output_int = plugboard.get_output(input_int)
        return {"status": "success", "output": output_int}
    except Exception as e:
        return {"status": "failure", "reason":str(e)}