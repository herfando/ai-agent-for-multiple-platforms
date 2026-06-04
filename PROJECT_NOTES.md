# Project Notes

## Start Backend

1. Activate virtual environment
   source venv/Scripts/activate

2. Start Docker (Redis, DB, dll)
   docker compose up -d

3. Run backend (FastAPI server)
   uvicorn main:app --reload

4. Run AI Worker (BACKGROUND PROCESS)
   python worker.py

5. Swagger API Docs

http://localhost:8000/docs

6. Update requirements.txt
   pip freeze > requirements.txt

## Stop Backend

1. Stop backend
   Ctrl + C

2. Stop Docker
   docker compose down

## Last Progress

Date:
Current Task:
Next Task:
