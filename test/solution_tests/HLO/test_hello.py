# from solutions.SUM import sum_solution
from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        
        assert hello_solution.hello('John') == "Hello, John!"
