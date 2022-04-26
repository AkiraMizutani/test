import sys
import random

value = sys.argv[1:]
for word in value:
    if len(word) > 3:
        s_list = [s for s in word]
        new_word = ""
        new_word += s_list.pop(0)
        while len(s_list) > 1:
            pick_index = random.randrange(0, len(s_list)-1)
            new_word += s_list.pop(pick_index)
        new_word += s_list.pop(0)
        print(new_word, end = ' ')
        
    else:
        print(word, end = ' ')
print()
