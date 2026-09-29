# bmi_calc.py bmi 계산 함수 소스코드


def bmi(height_cm: int, weight_kg: int) -> float:
    height_m = height_cm / 100.0
    val = weight_kg / (height_m ** 2)
    return round(val, 1)


def bmi_result(value: float) -> str:

    if value < 18.5:
        return "저체중"
    elif 18.5 <= value < 23.0:
        return "정상"
    elif 23.0 <= value < 25.0:
        return "과체중"
    else:
        return "비만"
