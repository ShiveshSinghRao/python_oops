"""
FASTAPI + SERVICE + COMPOSITION
"""

from fastapi import FastAPI, Depends

app = FastAPI()

class DB:
    def get_data(self):
        return "data"

class Service:
    def __init__(self, db):
        self.db = db

    def process(self):
        return f"Processed {self.db.get_data()}"

def get_db():
    return DB()

def get_service(db = Depends(get_db)):
    return Service(db)

@app.get("/")
def read(service: Service = Depends(get_service)):
    return {"result": service.process()}