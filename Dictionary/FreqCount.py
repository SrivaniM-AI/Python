def freq_count(text):
    freq = {}
    for ch in text:
        if ch == ' ':
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
            
print(freq_count("blah blah blah"))
    
        