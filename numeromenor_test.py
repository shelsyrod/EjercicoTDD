from numeromenor import menor

def test_menor():
    assert menor([5,4,3,2,1]) == 1
    assert menor([1,1,1,1,1]) == 1
    assert menor([1,2,3,4,5,6,7,8,9,10]) == 1
    assert menor([10,9,8,7,6,5,4,3,2,1]) == 1