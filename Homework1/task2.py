def bools():
    A = 1
    B = 0
    C = A and B   #false
    D = A and not B  #true
    E = A or B   #true
    return (C, D, E)

def integers():
    A = 1
    B = 2
    C = -1
    D = A + B #3
    E = A - B #-1
    F = (A + B) * C #-3
    G = A/B *C * -2*(B/4) #1/2
    return (D, E, F, G)
def test_bools():
    assert bools() == (0, 1, 1)
def test_integers():
    assert integers() == (3, -1, -3, 1/2)