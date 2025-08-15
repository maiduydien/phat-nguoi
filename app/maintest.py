# main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Đặt tên rõ ràng để tránh nhầm
from app.api.endpoints import router as api_router
from app.api.endpoints import routerOpenAI as openai_router

app = FastAPI(
    title="Tra cứu vi phạm giao thông",
    version="1.0.0",
)

# ---- CORS config (linh hoạt qua ENV) ----
# Ví dụ ALLOWED_ORIGINS="http://localhost:3000,https://your-frontend.com"
_allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
_allowed_origins = [o.strip() for o in _allowed_origins if o.strip()]
_allow_credentials = os.getenv("ALLOW_CREDENTIALS", "true").lower() == "true"

# Nếu muốn mở hoàn toàn (bao gồm credentials), dùng allow_origin_regex
# (FastAPI không cho allow_origins=["*"] khi allow_credentials=True)
if any(o == "*" for o in _allowed_origins):
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=".*",
        allow_credentials=_allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_allowed_origins,
        allow_credentials=_allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# ---- Mount routers ----
# Các route từ endpoints.py (ví dụ: /search)
app.include_router(api_router, tags=["Violations"])

# Các route OpenAI/Gemini: sẽ nằm dưới prefix /openai (ví dụ: /openai/fine)
app.include_router(openai_router, prefix="/openai", tags=["OpenAI Fine Info"])

# ---- Healthcheck ----
@app.get("/healthz", tags=["Health"])
def healthz():
    return {"status": "ok"}

# ---- Local run ----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=True
    )