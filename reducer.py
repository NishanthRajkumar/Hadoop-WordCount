import sys
from operator import itemgetter

current_word = None
current_count = 0
word = None

# input from console
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word: <15}\t{current_count}")
        current_count = count
        current_word = word

# Finally output the word to console
if current_word == word:
    print(f"{current_word}\t{current_count}")