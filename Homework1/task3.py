def is_positive (x):
    if(x>0):
        return 1
    if(x<0):
        return -1
    else:
        return 0

def print_primes():
    prime_list = [1, 2, 3]
    print("1"+"\n")
    print("2"+"\n")
    print("3"+"\n")
    primes = 3
    current = 4
    while (primes !=10):
        if(check_prime(current)):
            prime_list.append(current)
            print(str(current) + "\n")
            primes = primes +1
            current = current +1
            
        else:
            current = current +1

    return prime_list;

    

def check_prime(j):
    is_prime = 1;
    i = 2
    for i in range(2,j):
        if(j%i ==0):
            #notprime
            return 0
        
    
    return 1;

def test_print_primes():
    assert print_primes() == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]