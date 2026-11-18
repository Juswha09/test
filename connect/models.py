from sqlmodel import Field , SQLModel

class Users(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    username: str
    passwrod: str

class LoginSession(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    token_hashed: str
    expires_at: int

class Survey(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    Name: str
    Age: int
    Birthday: str
    Gender: str
    Email: str
    CN: str
    Work: str
    YE: str
    Achivements: str
    Address:str