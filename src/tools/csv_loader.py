import csv
from tools.models import Skill

def get_skills(excelPath: str = "input/course_skill.csv") -> list[Skill]:
    skills: list[Skill] = []
    with open(excelPath, encoding="utf-8", mode="r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for i, item in enumerate(reader):
            skills.append(Skill(
                Id=int(item[0]),
                Title=item[1]
            ))
    return skills

