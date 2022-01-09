import pytest


@pytest.fixture()
def setup():
    print('I will run first')
    yield
    print(" executed after the method")

@pytest.fixture(scope="class")
def class_setup():
    print("I will execute only once before class")
    yield
    print("I will execute only once after class")
    
@pytest.fixture()
def dataloader():
    return ['username','password','login']

#to run multiple times with different data set
@pytest.fixture(params=["chrome","firefox","IE"])
def crossbrowser(request):
    return request.param

