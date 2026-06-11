def char_frequency(text):
    unique_chars = []
    counts = []
    for ch in text:
        if ch not in unique_chars:
            unique_chars.append(ch)
            counts.append(1)
        else:
            index = unique_chars.index(ch)
            counts[index] += 1
    return unique_chars, counts

text = "banana"
if not text:
    print("Text is None")
else: 
    unique_chars, counts = char_frequency(text)
    for i in range(len(unique_chars)):
        print(unique_chars[i], '->', counts[i])