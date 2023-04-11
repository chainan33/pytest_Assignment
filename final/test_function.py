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

def test_calculateMonth_case7():
    #เกินเดือน OT เกิน
    assert calculateMonth(31, 4, 0) == 11380
