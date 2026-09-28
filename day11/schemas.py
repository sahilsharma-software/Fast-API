from pydantic import BaseModel, ConfigDict


class userCreate(BaseModel):
    username: str
    password: str


class userResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)


class userLogin(BaseModel):
    username: str
    password: str