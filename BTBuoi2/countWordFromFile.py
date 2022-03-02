from asyncio.windows_events import NULL
from queue import Empty


f = open('./text.txt', 'r', encoding='utf8')
text = f.read()

text1 = ''
for i in text:
    if ord(i) <= 47 and ord(i) >= 33 or ord(i) <= 64 and ord(i) >= 58 or ord(i) <= 96 and ord(i) >= 91 or ord(i) <= 126 and ord(i) >= 123:
        text1 = text1 + chr(32)
    else:
        text1 = text1 + i

text2 = ''
for i in range(0, len(text1.split(" "))):
    if text1[i] == "" and text1[i+1] != "":
        text2 = text2 + " "
        continue
    elif text1[i] == "":
        continue
    else:
        text2 = text2 + text1[i]

print(text2)
d = dict()


# str = 'Hello Binh/      Ga.'
# str1 = str.replace('/', ' ')
# print(str1.split(" "))