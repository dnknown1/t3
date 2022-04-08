import tests.test_simple_functions as tsf
import tests.test_mixed_functions as tmf

suites = [tsf, tmf]
TESTS = map(lambda suite: suite.tests, suites)
