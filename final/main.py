from function import calculateMonth

def main():
    # input
    daysWorked = int(input("จำนวนวันที่เข้าทำงาน : "))
    otHours = int(input("จำนวน OT ที่ได้ทำ : "))
    daysLate = int(input("จำนวนการมาทำงานสาย : "))

    monthly_compensation = calculateMonth(daysWorked, otHours, daysLate)
    #แสดงผล
    print(f"ค่าตอบแทนรายเดือนจำนวน {monthly_compensation} บาท.")

if __name__ == '__main__':
    main()

# from function import calculate_salary

# def main():
#     work_day = int(input("Enter work days: "))
#     ot_hour = int(input("Enter OT hours: "))
#     late_day = int(input("Enter late days: "))
#     print(f"Monthly salary: {calculate_salary(work_day, ot_hour, late_day):,.2f} THB")

# if __name__ == '__main__':
#     main()
