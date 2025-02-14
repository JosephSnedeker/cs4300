def calculate_discount(price, discount):
    if isinstance(price, str):
        if "$" in price:
            price = price.replace("$", "")
    
    price = float(price)
    if isinstance(discount,str):
        if "%" in discount:
            discount = discount.replace("%", "")
            discount = float(discount)
            discount = 1-(discount/100)
    discount = float(discount)
    return price * discount

def test_calculate_discount():
    assert calculate_discount("$1", "50%") == .5
    assert calculate_discount(4.00, .25) == 1
    assert calculate_discount(2, "50%") == 1
    assert calculate_discount("$4.00", "75%") == 1 #same as 4.00 and .25