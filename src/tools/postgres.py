import psycopg2
from tools.models import Video
import logging

DATABASE = "edwica"
TABLE = "skill_video"
HOST = "127.0.0.1"
PORT = "5432"
USER = "postgres"
PASSWORD = "admin"

COLUMNS_COUNT = 9

def connect() -> psycopg2.extensions.connection | None:
    try:
        connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    except BaseException as err:
        logging.fatal(err)
        connection = None
    finally:
        return connection 
    
def create_table():
    conn = connect()
    cur = conn.cursor()
    query = f"""create table if not exists {TABLE}(
        id serial,
        skill_id int not null,
        skill_name text not null,
        video_title text not null,
        url text not null,
        primary key (skill_id, url));"""
    try:
        cur.execute(query)
        conn.commit()
    except BaseException as err:
        logging.err(f"Ошибка добавлении данных: {err}")
    finally:
        conn.close()

def save_video(video: Video):
    conn = connect()
    cur = conn.cursor()
    query = f"INSERT INTO {TABLE} (skill_id, skill_name, video_title, url) VALUES({video.SkillId}, '{video.SkillName}', '{video.Title}', '{video.Url}')"
    try:
        cur.execute(query)
        conn.commit()
        logging.info(f"Успешно сохранили видео: [{video.Title}]")
    except BaseException as err:
        logging.error(f"Ошибка при сохранении: {err}")
    finally:
        conn.close()