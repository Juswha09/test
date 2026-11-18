from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import Users,Survey

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{id}")
async def read_employee(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Users, id)
        return {"message": user}
    

@app.post("/users")
async def root(users  : Users):
    with Session(engine) as session:
        session.add(users)
        session.commit()
        session.refresh(users)
        return {"message": users}
    
@app.get("/Survey/{id}")
async def read_survey(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Survey, id)
        return {"message": Survey}
    
@app.post("/Survey")
async def root(survey  : Survey):
    with Session(engine) as session:
        session.add(survey)
        session.commit()
        session.refresh(Survey)
        return {"message": Survey}
    
    
