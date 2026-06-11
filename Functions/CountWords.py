def count_words(text):
    if text.strip() == '':
        return 0
    words = 1
    for i in range(1, len(text)):
        if text[i].strip() != '' and text[i-1].strip() == '':
            words += 1 
    return words   
    
print(count_words("dsfsdf dfsdfsdf sdfsdfsd"))