import pytest


def test_subtract(setup):
    a = 7
    b = 9
    print(b - a)
    assert b - a == 2, "subtract failed"


@pytest.mark.usefixtures("dataloader")
def test_dataloading(dataloader):
    print(dataloader)
    print(dataloader[0])
    print(dataloader[2])

#to run multiple times with different data set
@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser(crossbrowser):
    print(crossbrowser)
