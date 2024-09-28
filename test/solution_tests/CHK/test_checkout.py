from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50

    def test_lots_of_A(self):
        assert checkout_solution.checkout('AAAA') == 180

    def test_bad_string(self):
        assert checkout_solution.checkout('bad string') == -1

    def test_bad_input(self):
        assert checkout_solution.checkout(67) == -1
    
    def test_group(self):
        assert checkout_solution.checkout('AAAABBBBCCCCDDDD') == 410

    def test_half(self):
        assert checkout_solution.checkout('AXA') == -1