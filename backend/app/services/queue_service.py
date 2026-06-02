import json
from app.core.redis import redis_client

QUEUE_NAME = "ai_jobs"


def push_ai_job(data: dict):
    redis_client.lpush(
        QUEUE_NAME,
        json.dumps(data)
    )