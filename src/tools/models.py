from typing import NamedTuple

class Video(NamedTuple):
    SkillId: int
    SkillName: str
    Title: str
    Url: str


class Skill(NamedTuple):
    Id: int
    Title: int