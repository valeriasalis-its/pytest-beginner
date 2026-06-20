def func(x):
    return x+1

def sum(x,y):
    return x+y

def test_answer():
    assert func(3) != 5

def test_sum():
    assert sum(3,5) == 8