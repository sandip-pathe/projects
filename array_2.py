heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
    