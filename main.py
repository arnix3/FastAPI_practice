from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index_page():
    return {"message": "Hello FastAPI!"}


@app.get("/item/{id}")
def get_item(id: int):
    return {"item_id": id, "message": f"item number {id} has been received!"}