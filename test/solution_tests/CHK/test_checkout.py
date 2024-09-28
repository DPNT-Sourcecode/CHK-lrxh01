from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50

    def test_lots_of_A(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_bad_string(self):
        assert checkout_solution.checkout('bad string') == -1

    def test_bad_input(self):
        assert checkout_solution.checkout(67) == -1
    
    def test_group(self):
        assert checkout_solution.checkout('AAAABBBBCCCCDDDD') == 410

    def test_half(self):
        assert checkout_solution.checkout('AxA') == -1

    def test_free_b(self):
        assert checkout_solution.checkout('EEEEBB') == 40+40+40+40

    def test_one_e(self):
        assert checkout_solution.checkout('E') == 40
    
    def test_all(self):
        assert checkout_solution.checkout('ABCDE') == 50+30+20+15+40

    def test_f(self):
        assert checkout_solution.checkout('F') == 10

    def test_f3(self):
        assert checkout_solution.checkout('FFF') == 20
    def test_f4(self):
        assert checkout_solution.checkout('FFFF') == 30
    def test_5u(self):
        assert checkout_solution.checkout('SSTXYYZ') == 80
    def test_letters(self):
        assert checkout_solution.checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 965