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
