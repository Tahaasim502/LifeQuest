from fastapi import FastAPI,Depends #same like include<iostream> header file we can access
from .databases import engine,Base,SessionLocal
from . import models,schemas
from sqlalchemy.orm import Session

app = FastAPI() #creating an object, just like oop which will be later used for calling functions 

def get_db():
    db = SessionLocal()
    
    try:
        yield db

    finally:
        db.close()

Base.metadata.create_all(bind = engine)

@app.get("/") #decorator it works in a way, of getting the stuff, each url is linked to a get, which is specific
def home():
    return {"message": "Welcome to LifeQuest API"} 


@app.post("/quests", response_model=schemas.QuestResponse) #this is the responce from the server we are giving to the user in the form of JSON
def create_quest(
    quest: schemas.QueryQuest,
    db: Session = Depends(get_db)
): 
    new_quest = models.Quest(title = quest.title)
    db.add(new_quest) #adding the quest after validating on the whiteboard
    db.commit() #saving the quest permanently
    db.refresh(new_quest) #since we know that id needs to refreshed after each quests 1 2...n, we are refreshing it 
    return new_quest

'''''
Visitor
   │
   ▼
Reception
   │
   ├── "/"        → Welcome desk
   ├── "/quests"  → Quest department
   ├── "/stats"   → Statistics department
   └── "/xp"      → XP department
'''''