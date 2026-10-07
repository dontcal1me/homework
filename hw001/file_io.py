# file_io.py
from bmi_calc import bmi, bmi_result

def read_health_data(file_name="health.txt"):
    people = []

    # 1. 파일 열기 (한글 깨짐 방지를 위해 cp949/utf-8 예외 처리)
    try:
        file = open(file_name, "r", encoding="utf-8")
    except UnicodeDecodeError:
        file = open(file_name, "r", encoding="cp949")

    # 2. 첫 번째 줄(제목 행: 전화번호 이름 키 몸무게) 읽어서 건너뛰기
    file.readline()

    # 3. 두 번째 줄부터 한 줄씩 읽어서 처리하기
    for line in file:
        line = line.strip()
        if not line:  # 빈 줄이 있으면 건너뜀
            continue

        data = line.split()

        phone = data[0]
        name = data[1]
        height = int(data[2])
        weight = int(data[3])

        # BMI 및 소견 계산
        val = bmi(height, weight)
        res = bmi_result(val)

        # 리스트에 추가
        people.append([phone, name, height, weight, val, res])

    # 4. 파일 닫기
    file.close()

    return people