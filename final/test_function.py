from function import calculateMonth


def test_calculateMonth_case1():
    #ไม่มี ot ไม่มีเลทงาน
    assert calculateMonth(20, 0, 0) == 6800

def test_calculateMonth_case2():
    #ไม่มี ot มีเลทงาน 
    assert calculateMonth(18, 0, 2) == 6120

def test_calculateMonth_case3():
    #มี OT ไม่มีเลทงาน
    assert calculateMonth(20, 3, 0) == 6980

def test_calculateMonth_case4():
    #มี ot มีเลทงาน
    assert calculateMonth(18, 3, 2) == 6300

def test_calculateMonth_case5():
    #ไม่มี ot ไม่มีเลทงาน
    assert calculateMonth(30, 0, 0) == 11200

def test_calculateMonth_case6():
    #เกินเดือน มีเลทงาน
    assert calculateMonth(31, 0, 1) == 10540

# import unittest
# from function import calculate_salary

# class TestCalculateSalary(unittest.TestCase):
#     def test_calculate_salary_no_ot_no_late(self):
#         self.assertAlmostEqual(calculate_salary(22, 0, 0), 7480.00)

#     def test_calculate_salary_with_ot_no_late(self):
#         self.assertAlmostEqual(calculate_salary(22, 2, 0), 8380.00)

#     def test_calculate_salary_no_ot_with_late(self):
#         self.assertAlmostEqual(calculate_salary(20, 0, 2), 6240.00)

#     def test_calculate_salary_with_ot_and_late(self):
#         self.assertAlmostEqual(calculate_salary(20, 2, 2), 7140.00)

#     def test_calculate_salary_with_max_ot_and_no_late(self):
#         self.assertAlmostEqual(calculate_salary(22, 3, 0), 8740.00)

#     def test_calculate_salary_with_max_ot_and_late(self):
#         self.assertAlmostEqual(calculate_salary(20, 3, 2), 7540.00)

#     def test_calculate_salary_with_more_than_max_ot(self):
#         self.assertRaises(ValueError, calculate_salary, 22, 4, 0)

#     def test_calculate_salary_with_negative_values(self):
#         self.assertRaises(ValueError, calculate_salary, -1, 2, 0)
#         self.assertRaises(ValueError, calculate_salary, 22, -1, 0)
#         self.assertRaises(ValueError, calculate_salary, 22, 2, -1)

# if __name__ == '__main__':
#     unittest.main()
