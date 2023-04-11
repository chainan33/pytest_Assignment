


def calculateMonth(daysWorked: int, otHours: int, daysLate: int) -> float:
    # validate input
    if daysWorked < 0 or otHours < 0 or daysLate < 0:
        raise ValueError("Invalid input")

    #จำนวนวันที่ทำงาน
    if daysWorked >= 0 :
        salary_days_worked = daysWorked * 340

    #จำนวน ชม ที่ทำ OT
    if otHours <= 3:
        salary_ot_hours = otHours * 60
    else:
        otHours = 3
        salary_ot_hours = otHours * 60
        print("ไม่สามารถทำ OT ได้เกิน 3 ชม ถ้าเกิน 3 ชม จะคิดเป็น 3 ชม")

    # calculate bonus for not being late
    if  daysWorked >= 30 :
        if daysLate == 0 :
            salary_ot_bonus = daysLate = 1000
        else :
            salary_ot_bonus = daysLate = 0
    else :
        salary_ot_bonus = daysLate = 0



    #จำนวนวันที่ทำงานสาย
    total_salary = salary_days_worked + salary_ot_hours + salary_ot_bonus

    return total_salary

