# file_io.py
from bmi_calc import bmi, bmi_result

def read_health_data(file_name="health.txt"):
    people = []


    # 첫 번째 줄(제목 행) 건너뛰기 위해 1번 인덱스부터 반복
    for line in lines[1:]:
        line = line.strip()
        if not line:  # 빈 줄은 건너뜀
            continue

        data = line.split()

        phone = data[0]
        name = data[1]
        height = int(data[2])
        weight = int(data[3])

        value = bmi(height, weight)
        result = bmi_result(value)

        people.append([phone, name, height, weight, value, result])

    return people
