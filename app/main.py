from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

# from . import models
# from .database import engine
from .routers import post, user, auth, vote

'''
Tells Postgres to automatically generate and create the tables/columns base on what has been
found in the models.py file.
'''
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
