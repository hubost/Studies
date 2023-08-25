def replace_word():
    strWord = 'Just a test for word replacement.'
    print(strWord)
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(strWord.replace(word_to_replace, word_replacement))
replace_word()
