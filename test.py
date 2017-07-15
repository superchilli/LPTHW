def anti_vowel(text):
    new_text = text
    for x in text:
        if x in "aeiouAEIOU":
            new_text = new_text.replace(x,"")
    return new_text
print(anti_vowel('asdfghjkluio'))
