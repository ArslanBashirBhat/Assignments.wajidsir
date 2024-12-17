def longest_word(words):
    longest = ''
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    return longest, max_length

output = longest_word(['Arsalan','Kamran','Jibran','Moonis','Taha','Muheeb','Ifham'])
print(output)
