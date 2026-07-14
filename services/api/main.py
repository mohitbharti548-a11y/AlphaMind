from fastapi import FastAPI

app = FastAPI(
    title="AlphaMind API",
    version="1.0.0",
    description="AI Financial Intelligence Platform"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AlphaMind API 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }