from .databases import Base #foundation of tables 
from sqlalchemy import String, Integer, Boolean, Column #foundation for the data types and defines column



class Quest(Base):
    __tablename__ = "quests" #creating a table 
    
    id = Column(Integer, primary_key=True, index=True) #index is ture for faster searching , each quest has an id
    title = Column(String, index=True) #Quest name 
    xp = Column(Integer, default=10) #Complete and u gain XP, if not mentioned we are using default 10
    completed = Column(Boolean, default=False) #how many are completed 

