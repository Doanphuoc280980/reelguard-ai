from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from services import generate_mindful_nudge

app = FastAPI(
    title="ReelGuard AI Backend",
    description="API hỗ trợ trợ lý AI chống doomscrolling và nhắc nhở tâm lý cho người dùng.",
    version="1.0.0"
)

# Cấu hình CORS để cho phép Frontend (Netlify hoặc Mobile App) gọi API thoải mái
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Có thể giới hạn domain cụ thể trong môi trường production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Định nghĩa cấu trúc dữ liệu đầu vào (Request Body)
class SessionCheckRequest(BaseModel):
    session_duration_minutes: int
    categories: List[str]
    goals: List[str]

# Định nghĩa cấu trúc dữ liệu đầu ra (Response)
class NudgeResponse(BaseModel):
    should_pause: bool
    urgency_level: str
    nudge_message: str
    recommended_action: Optional[str] = None

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "ReelGuard AI API is running successfully!",
        "version": "1.0.0"
    }

@app.post("/api/v1/analyze-session", response_model=NudgeResponse)
def analyze_user_session(request: SessionCheckRequest):
    """
    Endpoint chính: Nhận thời gian lướt thực tế từ thiết bị/người dùng,
    sau đó gọi service AI để phân tích và trả về thông điệp nhắc nhở phù hợp.
    """
    try:
        if request.session_duration_minutes < 0:
            raise HTTPException(status_code=400, context="Thời gian lướt không được nhỏ hơn 0.")
            
        # Gọi hàm xử lý AI từ services.py
        result = generate_mindful_nudge(
            session_duration=request.session_duration_minutes,
            categories=request.categories,
            goals=request.goals
        )
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý hệ thống: {str(e)}")
