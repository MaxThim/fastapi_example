from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from routers.todos import router as todos_router

app = FastAPI()

# Go to http://localhost:8000/docs to see the Swagger UI
# Go to http://localhost:8000/redoc to see the ReDoc UI
# To run program, type "uvicorn main:app --reload" in terminal

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}



