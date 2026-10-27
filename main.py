from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ReelSession, NudgeResponse
from services import generate_mindful_nudge
from config import settings

app = FastAPI(
    title="ReelGuard AI API",
    description="Backend API cho trợ lý lướt mạng xã hội lành mạnh - Meta Global AI Developer Hackathon",
    version="1.1.0"
)

# Thêm cấu hình CORS để cho phép trang web Netlify gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "project": "ReelGuard AI",
        "status": "Active",
        "hackathon": "Meta Global AI Developer Hackathon 2026",
        "track": "Build for Your World"
    }

@app.post("/api/v1/analyze-session", response_model=NudgeResponse)
def analyze_user_session(session: ReelSession):
    """
    Endpoint nhận dữ liệu phiên lướt từ client, kiểm tra ngưỡng thời gian và kích hoạt Meta Model API để trả về lời nhắc phù hợp.
    """
    if session.session_duration_minutes < settings.WARNING_THRESHOLD_MINUTES:
        return NudgeResponse(
            should_pause=False,
            urgency_level="low",
            nudge_message="Thời gian lướt đang ở mức an toàn. Hãy giữ sự cân bằng nhé!",
            recommended_action=None
        )
    
    nudge_data = generate_mindful_nudge(
        session.session_duration_minutes,
        session.watched_categories,
        session.user_goals
    )
    return nudge_data
