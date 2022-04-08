from functools import reduce
from operator import add
import tests.register as register
from util import uDecorators as ud

REGESTERED_TESTS = reduce(add, register.TESTS)

def tester(test) -> None:
    r, m = test()
    assert r, m

@ud.timer
def run_tests(tests: REGESTERED_TESTS):
    if tests:
        tester(tests[0])
        return run_tests(tests[1:])
    return True

t, _ = run_tests(REGESTERED_TESTS)
print(t, len(REGESTERED_TESTS), 'Tests')
