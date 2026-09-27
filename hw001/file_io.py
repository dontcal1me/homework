# file_io.py 파일 입출력을 담당하는 소스코드
import os

def read_health_data(file_name: str = "health.txt") -> list[dict]:
    # file_io.py가 있는 폴더(hw001)의 절대 경로를 구함
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    # 인코딩 예외 처리 (utf-8 실패 시 cp949)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp949') as f:
            lines = f.readlines()
    data = []   
    for line in lines:
        line = line.strip()
        # 헤더이거나 빈 줄 건너뛰기
        if not line or line.startswith("전화번호"):
            continue
            
        parts = line.split()
        if len(parts) >= 4:
            data.append({
                "phone": parts[0],
                "name": parts[1],
                "height": int(parts[2]),
                "weight": int(parts[3])
            })
            
    return data