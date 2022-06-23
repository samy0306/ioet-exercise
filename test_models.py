import pytest
from models.employee import employee
from models.schedule import schedule  

def test_employee_model():
    mockedListTimes = ["TU10:00-12:00","MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"]
    schedules_array = employee.getEmployee('', mockedListTimes)
    type_object = type(schedules_array[0])

    assert type(schedules_array) == type(mockedListTimes)
    assert type_object == type(schedule('', '', ''))

def test_schedule_model():
    scheduleMocked = schedule('MO', '12:00', '13:00')

    assert type(scheduleMocked) == type(schedule('', '', ''))