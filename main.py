from controller.payroll_controller import payroll
from controller.controller import controller

controller.calculateMatch(payroll.getPayroll("input.txt"))


