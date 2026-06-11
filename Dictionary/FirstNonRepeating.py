def first_non_repeating(text):
    freq = {}
    for ch in text:
        if ch == ' ':
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in text:
        if ch != ' ' and freq[ch] == 1:
            return ch
    
    return None
        
print(first_non_repeating('blah blah'))