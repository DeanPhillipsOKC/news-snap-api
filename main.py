from dotenv import load_dotenv
from fastapi import FastAPI
from routers import feeds


app = FastAPI()
app.include_router(feeds.router)

