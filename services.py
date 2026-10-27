import requests
from config import settings

def generate_mindful_nudge(session_duration: int, categories: list, goals: list) -> dict:
    prompt = (
        f"Người dùng đã lướt Facebook Reels liên tục trong {session_duration} phút qua, "
        f"tập trung vào các chủ đề: {', '.join(categories)}. "
        f"Mục tiêu quan trọng của họ hôm nay là: {', '.join(goals)}. "
        "Hãy đóng vai trợ lý AI thấu cảm của ReelGuard AI, viết một thông điệp nhắc nhở nhẹ nhàng nhưng sâu sắc, "
        "giúp họ nhận thức được thời gian và truyền cảm hứng để họ quay lại với mục tiêu thực tế."
    )

    payload = {
        "model": "muse-spark",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {settings.META_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Tích hợp thực tế Meta Model API khi có key chính thức
        # response = requests.post(settings.META_API_URL, json=payload, headers=headers, timeout=10)
        # data = response.json()

        if session_duration >= settings.CRITICAL_THRESHOLD_MINUTES:
            return {
                "should_pause": True,
                "urgency_level": "high",
                "nudge_message": f"Đã {session_duration} phút trôi qua rồi bạn ơi! Các video về {categories[0] if categories else 'giải trí'} đang chiếm trọn thời gian. Mục tiêu '{goals[0] if goals else 'hoàn thành công việc'}' đang chờ bạn. Hãy tạm dừng nhé!",
                "recommended_action": "Khóa ứng dụng Reels trong 30 phút"
            }
        else:
            return {
                "should_pause": True,
                "urgency_level": "medium",
                "nudge_message": f"Hey, bạn đã lướt {session_duration} phút rồi. Tạm dừng một nhịp, hít thở sâu và xem xét lại mục tiêu '{goals[0] if goals else 'chính'}' của ngày hôm nay nào!",
                "recommended_action": "Đứng dậy đi lại trong 2 phút"
            }

    except Exception as e:
        return {
            "should_pause": False,
            "urgency_level": "low",
            "nudge_message": "Hãy tận hưởng trải nghiệm lướt mạng xã hội một cách tỉnh táo và có kiểm soát.",
            "recommended_action": None
        }
