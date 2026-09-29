# main.py
from file_io import read_health_data
from drawer import draw_table_and_data

def main():
    # health.txt 파일 읽기 및 BMI 데이터 리스트 생성
    people = read_health_data("health.txt")

    # Turtle 그래픽 표 출력
    draw_table_and_data(people)

if __name__ == "__main__":
    main()
