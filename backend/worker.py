import json
import time

from app.core.redis import redis_client
from app.db.database import SessionLocal

from app.services.ai_service import generate_ai_reply
from app.services.intent_service import detect_intent
from app.services.conversation_state_service import (
    get_or_create_state,
    update_state
)

from app.services.response_service import build_response
from app.services.response_router import route_response

from app.models.ai import AIMemory

QUEUE_NAME = "ai_jobs"


def process_job(job):

    db = SessionLocal()

    try:
        print("Processing job:", job)

        conversation_id = job["conversation_id"]
        content = job["content"]

        # 🔵 1. STATE
        state = get_or_create_state(db, conversation_id)

        # 🔵 2. INTENT DETECTION
        intent = detect_intent(content)

        # 🔵 3. UPDATE STATE
        update_state(db, state, content, intent)

        # 🔵 4. MEMORY LOAD
        memory = db.query(AIMemory).filter(
            AIMemory.contact_id == conversation_id
        ).first()

        memory_text = memory.memory if memory else ""

        # 🔵 5. AI GENERATION (GROQ)
        ai_reply = generate_ai_reply(
            content,
            state,
            memory_text
        )

        # 🔵 6. BUILD RESPONSE OBJECT
        response = build_response(ai_reply)

        # 🔵 7. ROUTE KE PLATFORM
        route_response(
            "instagram",
            response,
            conversation_id
        )

        print("INTENT:", intent)
        print("AI REPLY:", ai_reply)

    except Exception as e:
        print("Error processing job:", str(e))

    finally:
        db.close()


def worker_loop():
    print("AI Worker started...")

    while True:
        job = redis_client.rpop(QUEUE_NAME)

        if job:
            try:
                data = json.loads(job)
                process_job(data)
            except Exception as e:
                print("Invalid job format:", str(e))
        else:
            time.sleep(1)


if __name__ == "__main__":
    worker_loop()