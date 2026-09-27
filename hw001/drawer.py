# drawer.py 출력 표 화면을 담당하는 소스코드

import turtle

def draw_table_and_data(records: list[dict]):
    """
    Turtle을 사용하여 헤더와 데이터를 표 형태로 출력합니다.
    """
    screen = turtle.Screen()
    screen.title("BMI 프로그램 (Turtle Graphic)")
    screen.setup(width=900, height=500)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()

   
    headers = ["전화번호", "이름", "키 (cm)", "몸무게(kg)", "BMI", "소견"]
    col_widths = [160, 90, 90, 110, 80, 80]
    
    start_x = -320
    start_y = 150
    row_height = 35

    # 1. 헤더 출력
    curr_x = start_x
    for i, header in enumerate(headers):
        t.goto(curr_x, start_y)
        t.write(header, align="left", font=("맑은 고딕", 11, "bold"))
        curr_x += col_widths[i]

    # 구분선 (헤더 아래 선)
    t.goto(start_x, start_y - 10)
    t.pendown()
    t.pensize(2)
    t.goto(start_x + sum(col_widths), start_y - 10)
    t.penup()
    t.pensize(1)

    # 2. 레코드 데이터 출력
    current_y = start_y - row_height - 5
    for rec in records:
        # BMI 출력 시 정수/소수점 형태 그대로 문자열 변환
        bmi_str = str(rec["bmi"]) if rec["bmi"] % 1 != 0 else str(int(rec["bmi"]))
        
        row_values = [
            rec["phone"],
            rec["name"],
            str(rec["height"]),
            str(rec["weight"]),
            bmi_str,
            rec["status"]
        ]
        
        curr_x = start_x
        for i, val in enumerate(row_values):
            t.goto(curr_x, current_y)
            t.write(val, align="left", font=("맑은 고딕", 10, "normal"))
            curr_x += col_widths[i]
            
        current_y -= row_height

    screen.mainloop()