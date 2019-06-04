def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not epect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
def test_between(smallest, highest, item):
    assert smallest <= item and highest >= item, "Expected {0} to be between or equal to {1} and {2}".format(item, smallest, highest)
    
test_between(5, 25, 5)    
    
test_not_in([1,2,3,4,5,6,7,8,9], 5)
    
test_is_in([1,2,3,4,5,6], 9)    

 
    
  