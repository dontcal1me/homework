from file_io import read_health_data
from bmi_calc import calculate_bmi
from drawer import draw_table_and_data

def main():
    records = read_health_data("health.txt")

    for rec in records:
        bmi, status = calculate_bmi(rec["height"], rec["weight"])
        rec["bmi"] = bmi
        rec["status"] = status

    draw_table_and_data(records)

if __name__ == "__main__":
    main()