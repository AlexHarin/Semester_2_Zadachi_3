with open('sample.txt', 'r') as file:
    text = file.read()

text = text.lower().replace('\n', ' ').replace(',', '').replace('.', '')

words = text.split()

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

avg_word_length = sum(len(word) for word in words) / len(words)

print('Частота слов:')
for word, freq in word_freq.items():
    print(f'{word}: {freq} раз')
print(f'Средняя длина слова: {avg_word_length}')
