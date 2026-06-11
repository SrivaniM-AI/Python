def reverse_string(text):
    reverse_str = ''
    for ch in text:
        reverse_str = ch + reverse_str
    return reverse_str

print(reverse_string('Python'))