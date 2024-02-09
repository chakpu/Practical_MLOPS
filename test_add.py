import sys, os
sys.path.insert(0, os.getcwd())

from script import addition

def test_add():
    ans = addition(3,4)
    assert ans == 7