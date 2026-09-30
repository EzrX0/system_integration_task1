from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model data
class student(BaseModel):
    name : Optional[str] = None
    address : Optional[str] = None
    gpa : Optional[int] = None
    semester : Optional[int] = None
    hobby : Optional[str] = None


#db 
items_db = {}


#ROOT
@app.get("/")
def read_root():  
    return {"message" : "Hello YOU"}

#Create POST
@app.post("/student/{item_id}")
async def create_item(item_id: int, item: student):
    if item_id in items_db:
        return {"error" : "this student is already registered"}
    items_db[item_id] = item.model_dump()
    return {"message" : "Student registered successfully", "item": items_db[item_id]}

#Read GET
@app.get("/student/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db :
        raise HTTPException(status_code = 404, detail = "student not found")
    return {"item_id" : item_id, "item" : items_db[item_id]}

#Update PUT
@app.put("/student/{item_id}")
async def update_item(item_id: int , item: student):
    if item_id not in items_db:
        return {"error" : "Item not found"}
    items_db[item_id] = item.model_dump()
    return {"message" : "Item updated successfully", "item" : items_db[item_id]}

#Delete DELETE
@app.delete("/student/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        return {"error" : "student not found"}
    deleted_item = items_db.pop(item_id)
    return {"nessage" : "student deleted successfully", "deleted_item": deleted_item}