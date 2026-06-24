values = [0, 1, '', 'hello', [], [1, 2], None, 3.14]

for value in values:
    if value:
        truth_value = "Truthy"
    else:
        truth_value = "Falsy"

    print(f"Value: {value} and Truthiness: {truth_value}")
    
    