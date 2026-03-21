"""
FASTAPI DEPENDENCY INJECTION
"""

from fastapi import FastAPI, Depends

app = FastAPI()

class DB:
    def get_data(self):
        return "data"

def get_db():
    return DB()

@app.get("/")
def read(db: DB = Depends(get_db)):
    return {"data": db.get_data()}