from pydantic import BaseModel, Field
from typing import List, Optional

class ReelSession(BaseModel):
    user_id: str = Field(..., description="ID định danh người dùng")
    session_duration_minutes: int = Field(..., ge=0, description="Thời gian đã lướt tính bằng phút")
    watched_categories: List[str] = Field(..., description="Danh mục video đã xem (VD: comedy, tech, lifestyle)")
    user_goals: List[str] = Field(..., description="Mục tiêu trong ngày của người dùng")

class NudgeResponse(BaseModel):
    should_pause: bool
    urgency_level: str  # 'low', 'medium', 'high'
    nudge_message: str
    recommended_action: Optional[str] = None
