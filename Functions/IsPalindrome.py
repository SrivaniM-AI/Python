def is_palindrome(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text

    return text == reversed_text

print(is_palindrome("madam"))