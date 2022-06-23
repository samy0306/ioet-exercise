import pytest
from datetime import datetime
from controller.controller import controller
from controller.payroll_controller import payroll
from models.schedule import schedule  

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        ([schedule("MO",datetime.strptime("10:15","%H:%M"),datetime.strptime("12:00","%H:%M"))], [schedule("MO",datetime.strptime("11:15","%H:%M"),datetime.strptime("12:00","%H:%M"))], 1),
        ([schedule("MO",datetime.strptime("10:00","%H:%M"),datetime.strptime("12:00","%H:%M")),schedule("TH",datetime.strptime("12:00","%H:%M"),datetime.strptime("14:00","%H:%M")),schedule("SU",datetime.strptime("20:00","%H:%M"),datetime.strptime("21:00","%H:%M"))], [schedule("MO",datetime.strptime("10:15","%H:%M"),datetime.strptime("12:00","%H:%M")),schedule("TU",datetime.strptime("10:00","%H:%M"),datetime.strptime("12:00","%H:%M")),schedule("TH",datetime.strptime("13:00","%H:%M"),datetime.strptime("13:15","%H:%M")),schedule("SA",datetime.strptime("14:00","%H:%M"),datetime.strptime("18:00","%H:%M")),schedule("SU",datetime.strptime("20:00","%H:%M"),datetime.strptime("21:00","%H:%M"))] , 3),
    ]
)
def test_compare_arrays(input_a, input_b, expected):
    assert controller.compare_Arrays(input_a, input_b) == expected

def test_payrollController():
    employees_payroll = payroll.getPayroll("input.txt")
    data_out = ''
    type_data = ''
    for i in employees_payroll:
        data_out += i.name
        type_data = type(i.times)

    assert data_out == 'RENEASTRIDANDRESJUANNACHOCHINO'
    assert type_data == type(list())
