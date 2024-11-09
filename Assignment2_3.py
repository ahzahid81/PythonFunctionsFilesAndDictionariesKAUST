str1 = 'I wish I wish with all my heart to fly with dragons in a land apart'
freq_words = None
freq_words = {}

for word in str1.split():
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
    
    
print(freq_words)