import force_brackets
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_pass_good(self):
        try:
            force_brackets.enable()
            success = True
            pass
        except SyntaxError, e:
            success = False
            print e
            pass

        self.assertTrue(success)
        pass

    def test_pass_bad(self):
        try:
            force_brackets.enable()
            success = False
        except SyntaxError:
            success = True

        self.assertTrue(success)

    def test_curly_good(self): #{
        try: #{
            force_brackets.enable(1)
            success = True
        #}
        except SyntaxError, e: #{
            success = False
            print e
        #}

        self.assertTrue(success)
    #}

    def test_curly_bad(self):
        try:
            force_brackets.enable(1)
            success = False
        except SyntaxError:
            success = True

        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()

