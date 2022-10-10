# Напишите программу, удаляющую из текста все слова, содержащие "абв".

with open('task21_in.txt', 'r') as data:
    text_in = data.read()
text_in = list(filter(lambda x: 'абв' not in x, text_in.split()))
text_out = ' '.join(text_in)
with open('task21_out.txt', 'w') as data:
    data.write(text_out)
