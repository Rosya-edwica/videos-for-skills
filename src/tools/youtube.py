from youtubesearchpython import VideosSearch

from tools.models import Video, Skill


def find_video_for_skill(skill: Skill, limit: int = 3) -> list[Video]:
    videos: list[Video] = []
    youtube = VideosSearch(query=skill.Title, limit=limit)
    for item in youtube.result()["result"]:
        videos.append(Video(
            SkillId=skill.Id,
            SkillName=skill.Title,
            Title=item["title"],
            Url=item["link"]
        ))
    return videos
