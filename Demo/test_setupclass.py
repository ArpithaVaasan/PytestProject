import pytest


@pytest.mark.usefixtures("class_setup")
class TestFixture:
    def test_fix1(self):
        print("fix 1")

    def test_fix2(self):
        print("fix 2")

    def test_fix3(self):
        print("fix 3")

    def test_fix4(self):
        print("fix 4")
