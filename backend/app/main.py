from fastapi import FastAPI #same like include<iostream> header file we can access

app = FastAPI() #creating an object, just like oop which will be later used for calling functions 
@app.get("/") #decorator it works in a way, of getting the stuff, each url is linked to a get, which is specific
def home():
    return {"message: Welcome to LifeQuest API"} 



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