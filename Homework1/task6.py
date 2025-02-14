def count_words(file_name):
    file = open(file_name, "r")
    file = file.read()
    file = file.replace("\n", " ")
    file = file.replace(",", "")
    file = file.replace(".", "")
    word = len(file.split())   
    print(word)
    return word

count_words("task6_read_me.txt")
def test_count_words():
    assert count_words("task6_read_me.txt") == 104
