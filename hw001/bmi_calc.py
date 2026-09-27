# bmi_calc.py bmi 계산 함수 소스코드

def calculate_bmi(height_cm: float, weight_kg: float) -> tuple[float, str]:
    """키(cm)와 몸무게(kg)를 입력받아 BMI와 소견을 반환"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 1)

    if bmi_rounded < 18.5:
        status = "저체중"
    elif 18.5 <= bmi_rounded < 23.0:
        status = "정상"
    elif 23.0 <= bmi_rounded < 25.0:
        status = "과체중"
    else:
        status = "비만"

    return bmi_rounded, status