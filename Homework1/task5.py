
def book():    
    books = [["book1", "author1"], ["book2", "author2"], ["book3", "author3"], ["book4", "author4"]]
    print (books[0:3])
    return books[0:3]
def diction():
    students = {
        "name": "name1",
        "number": 1234
    }
    print(students)
    return 0
book()
diction()
def test_book():
    assert book() == [["book1", "author1"], ["book2", "author2"], ["book3", "author3"]]
def test_diction():
    assert diction() == 0
