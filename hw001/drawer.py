# drawer.py
import turtle

def draw_table_and_data(people):
    screen = turtle.Screen()
    screen.title("BMI 프로그램")
    screen.setup(width=850, height=500)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()

    headers = ["전화번호", "이름", "키 (cm)", "몸무게(kg)", "BMI", "소견"]
    col_widths = [150, 90, 90, 110, 80, 80]

    start_x = -300
    start_y = 150
    row_height = 35

    # 1. 헤더 출력
    curr_x = start_x
    for i, header in enumerate(headers):
        t.goto(curr_x, start_y)
        t.write(header, align="left", font=("맑은 고딕", 11, "bold"))
        curr_x += col_widths[i]

    # 구분선
    t.goto(start_x, start_y - 10)
    t.pendown()
    t.pensize(2)
    t.goto(start_x + sum(col_widths), start_y - 10)
    t.penup()
    t.pensize(1)

    # 2. 데이터 출력
    current_y = start_y - row_height - 5
    for person in people:
        curr_x = start_x
        for i, val in enumerate(person):
            t.goto(curr_x, current_y)
            t.write(str(val), align="left", font=("맑은 고딕", 10, "normal"))
            curr_x += col_widths[i]
        current_y -= row_height

    screen.mainloop()
