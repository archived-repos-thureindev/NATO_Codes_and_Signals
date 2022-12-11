import code_translator as translator

text = input("Text to translate: ")

print(translator.get_all(text))
print(translator.get_morse(text))
print(translator.get_alphabet(text))
print(translator.get_alphabet(text, include_phonetic=True))

