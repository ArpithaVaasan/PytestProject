# all test file should start or end with test_ or _test
# each method is a test case and method should also contain test_
import pytest

@pytest.mark.smoke
def test_demoTC1():
    print("hello")


@pytest.mark.skip
def test_demoTC2():
    msg = "Hello"
    assert msg == "Hi", "failed, strings do not match"



