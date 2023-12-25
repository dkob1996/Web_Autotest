from func import checkText

def test_step1(bad_word, good_word):
    assert good_word in checkText(bad_word), 'Test_1 Fail'
