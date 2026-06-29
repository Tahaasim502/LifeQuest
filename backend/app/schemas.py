from pydantic import BaseModel,Field, ConfigDict #Basemodel is used for API schema, filed is used for rules 


class QueryQuest(BaseModel):
    title : str = Field(
        min_length=3,
        max_length=100,
        description="Enter quest"
    )


class QuestResponse(BaseModel):
    id : int
    title : str
    xp : int
    completed : bool 

    model_config = ConfigDict(from_attributes=True) #Since it will accept pydantic model we are passing directly the objects of SQLalchemy, so it can read the attributes