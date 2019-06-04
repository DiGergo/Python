from byotest import *

usd_coins= [100, 50, 25, 10, 5, 1]
eur_coins= {100:20, 50:20, 20:20, 10:20, 5:0, 2:0, 1:8}

def get_change(amount, coins=eur_coins):
       
    change =[]
    
    for item in sorted(coins.keys(), reverse=True):
        while item <= amount and coins[item] > 0:
            amount -= item
            coins[item] -= 1
            change.append(item)
            
    if amount != 0:
        raise Exception("Not enough change")
        
    return change   
    
test_are_equal(get_change(0),[])    
test_are_equal(get_change(1),[1]) 
test_are_equal(get_change(2, {2:2}),[2]) 
#test_are_equal(get_change(5),[5]) 
test_are_equal(get_change(10),[10]) 
test_are_equal(get_change(20),[20]) 
test_are_equal(get_change(50),[50]) 
test_are_equal(get_change(100),[100]) 
#test_are_equal(get_change(9),[5, 2, 2]) 
test_are_equal(get_change(9), [1,1,1,1,1,1,1,1,1])

print ("All test pass!")        