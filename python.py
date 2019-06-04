def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
assert count_upper_case("A") == 1, "One uppercase"    
assert count_upper_case("") == 1, "Empty string"

print(count_upper_case("Hello World RFDSFDSDFSDF"))    