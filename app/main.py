
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS App Runner!"}