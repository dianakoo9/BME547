print("This is the database module and python calls it {}".format(__name__))

from blood_calculator import check_HDL, check_LDL

HDL_value = 55

classification = blood_calculator.check_HDL(HDL_value)
print("55 is {}".format(classification))
x = check_LDL(200)
