from combigraphs.combfuncs import fact

def combination(n, k):
    if (k == 0) or (n == k):
        return 1
    if (k == 1) or (k == n - 1):
        return n
    return (fact.factorial(n) // (fact.factorial(k) * fact.factorial(n - k)))

def test_combination():
    assert combination(4, 2) == 6
    print("test_combination complete!")
    
if __name__ == '__main__':
    test_combination()
    print(combination(10, 3))