import json
from app.core.redis import redis_client

QUEUE_NAME = "ai_jobs"


def push_message(conversation_id, content, platform):

    redis_client.lpush(
        QUEUE_NAME,
        json.dumps({
            "conversation_id": conversation_id,
            "content": content,
            "platform": platform
        })
    )