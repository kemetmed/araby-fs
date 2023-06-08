from pydantic.types import Optional, List
from sqlmodel import Field, Relationship, SQLModel

from api.public.team.models import Team
from api.utils.generic_models import HeroTeamLink


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Super Man",
                "secret_name": "Clark Kent",
                "age": 27,
                "team_id": 1,
            }
        }


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    teams: List[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    teams: List[Team] = None


class HeroUpdate(HeroBase):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    teams: List[Team] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Super Man",
                "secret_name": "Clark Kent",
                "age": 27,
                "team_id": 1,
            }
        }
