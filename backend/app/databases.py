from sqlalchemy import create_engine #enging is a door way, URL is the address that tells which door way we should open
from sqlalchemy.orm import sessionmaker, declarative_base #session maker is the workspace, delcrative base is base class for all the models(XP, Quest)
#so this right here is used for accessing the data 
#sqlite is the language we are using 
#:/// this is used for connection, every databse has different connection syntax
#./ look in the current projectory 
DATABASE_URL = "sqlite:///./lifequest.db" 


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Sessionlocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)


Base = declarative_base() #blue print for the objects