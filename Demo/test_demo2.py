import pytest


@pytest.mark.smoke
def test_demoTC2(setup):
    print('good morning')

@pytest.mark.xfail
def test_addition():
    a = 3
    b = 4
    print(a+b)
    assert a+b == 7,"addition failed"


