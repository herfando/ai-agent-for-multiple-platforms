import json
import time

from app.core.redis import redis_client

QUEUE_NAME = "ai_jobs"


def process_job(job):
    print("Processing:", job)

    # nanti sini kita panggil Groq (fase 22)
    time.sleep(2)


def worker_loop():
    print("AI Worker started...")

    while True:
        job = redis_client.rpop(QUEUE_NAME)

        if job:
            data = json.loads(job)
            process_job(data)
        else:
            time.sleep(1)


if __name__ == "__main__":
    worker_loop()