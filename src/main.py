import tools.csv_loader as csv_loader
import tools.youtube as youtube
import tools.postgres as postgres
from multiprocessing import Pool
from time import time

import logging

    
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.basicConfig(filename="info.log", filemode='w', datefmt='%H:%M:%S', level=logging.DEBUG, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
print("Logfile: info.log")

def main():
    print("Программа запущена!")
    logging.info("Программа запущена")
    
    skills = csv_loader.get_skills()
    for i in range(0, len(skills), 10):
        poll_items = skills[i:][:10]
        with Pool(10) as process:
            process.map_async(
                func=find,
                iterable=poll_items,
                error_callback=lambda x: print(x)
            )
            process.close()
            process.join()
        

def find(skill):
    videos = youtube.find_video_for_skill(skill)
    for video in videos:
        postgres.save_video(video)

if __name__ == "__main__":
    s = time()
    postgres.create_table()
    main()
    print(f"Time: {round(time()-s, 2)} seconds...")
