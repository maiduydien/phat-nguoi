from fastapi import FastAPI
from app.api.endpoints import router
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import routerOpenAI as fine_router






'''
try:
    open("app/services/violation_service1.py")
except FileNotFoundError:
    print("File not found, using default violation_service.py")
    raise
'''


app = FastAPI(title="Tra cứu vi phạm giao thông")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Cho phép React gọi API
    allow_credentials=True,
    allow_methods=["*"],                      # Cho phép mọi phương thức (GET, POST...)
    allow_headers=["*"],                      # Cho phép mọi loại header
)
app.include_router(router)
app.include_router(fine_router, prefix="/openai", tags=["OpenAI Fine Info"])

    



