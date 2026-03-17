from fastapi import FastAPI
app=FastAPI()
test=[]
@app.get("/")
def read_root():
  return {"message":"Welcome to TutoratUp API!"}
@


  