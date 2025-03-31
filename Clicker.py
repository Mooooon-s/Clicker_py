import pyautogui
import time
from datetime import datetime, timedelta

# === [1] 설정 ==========================
click_x = 1046  # 예약하기 버튼의 X 좌표
click_y = 1202  # 예약하기 버튼의 Y 좌표
target_datetime_str = "2025-03-31 23:22:30"  # 목표 시간 (년-월-일 시:분:초)
buffer_check_seconds = 10
# ======================================

def get_korean_local_time():
    """현재 시스템의 시간을 한국 시간으로 보정"""
    return datetime.now() + timedelta(hours=9 - time.localtime().tm_gmtoff // 3600)

# (1) 목표 시각 파싱
target_datetime = datetime.strptime(target_datetime_str, "%Y-%m-%d %H:%M:%S")

print("🟡 예약 매크로 대기 중... (PC 한국 시간 기준)")
print("🎯 목표 시간:", target_datetime.strftime("%Y-%m-%d %H:%M:%S"))

# (2) 대기 루프
while True:
    now = get_korean_local_time()
    delta = (target_datetime - now).total_seconds()
    print(f"⏱ 현재 시간: {now.strftime('%Y-%m-%d %H:%M:%S')} / 남은 시간: {delta:.2f}초", end="\r")

    if delta <= 0:
        pyautogui.click(click_x, click_y)
        print(f"\n✅ [{now.strftime('%Y-%m-%d %H:%M:%S')}] 예약하기 버튼 클릭 완료!")
        break

    if delta > buffer_check_seconds:
        time.sleep(1)
    else:
        time.sleep(0.00005)
