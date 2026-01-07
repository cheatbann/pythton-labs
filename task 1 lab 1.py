import string


def text_analyzer(text):
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sample_text = """
Python - це круто. Python дозволяє писати код швидко. 
Код на Python читається легко. Легко писати, легко читати.
Код, код, код, код. Python, python.
"""

frequency_dict = text_analyzer(sample_text)
frequent_words = [word for word, count in frequency_dict.items() if count > 3]

print("Повний словник частот:")
print(frequency_dict)
print("-" * 30)
print("Слова, що зустрічаються більше 3 разів:")
print(frequent_words)