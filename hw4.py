
def single_root_words(root_word, *other_words):
    same_word = []  # новый список
    root_w = root_word.upper() #верхний регистр
    for _ in other_words: #для каждого элемента списка
        _w = _.upper() # верхний регистр
        if root_w in _w:    # слова в списке содержат root_word
            same_word.append(_)
        if _w in root_w:  #root_word содержит одно из слов списка
            same_word.append(_)
    return same_word  #возвращаем список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)