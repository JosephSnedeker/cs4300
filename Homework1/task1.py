def helloworld():
    x = "Hello, World"
    print(x)
    return x

def test_hello():
    assert helloworld() == "Hello, World"