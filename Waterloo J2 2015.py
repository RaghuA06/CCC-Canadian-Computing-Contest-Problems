# Raghu Alluri
# Happy = :-)   Sad = :-(

feeling = input()
happy = ":-)"
sad = ":-("

h = feeling.count(happy)
s = feeling.count(sad)

if h > s:
    print('happy')
elif h < s:
    print('sad')
elif h == s == 0:
    print('none')
elif h == s:
        print('unsure')
