# from solutions.SUM import sum_solution
from lib.solutions.HLO import hello_solution


class HelloTest():
    def hello_test(self):
        assert hello_solution.hello('Test string') == 'Test String'


