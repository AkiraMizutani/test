text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
table = text.maketrans({',': '', '.': ''})
new_text = text.translate(table)
word_list = new_text.split(' ')
print([len(i) for i in word_list])