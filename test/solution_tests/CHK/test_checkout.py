from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50

    def test_lots_of_A(self):
        assert checkout_solution.checkout('AAAA') == 180