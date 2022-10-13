# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def txt_encoder(my_txt):    
    code_txt = [my_txt[0], 1]
    for i in my_txt[1:]:
        if i != code_txt[-2]: 
            code_txt += [i, 1]
        else:
            code_txt[-1] += 1    
    return ''.join(map(str, code_txt))
def txt_decoder(my_txt):
    count = 0
    decode_txt =''
    char = my_txt[0]
    for i in my_txt[1:]:
        if i.isdigit():
            count = int(i)
            decode_txt += char * count
        else: char = i
    return decode_txt

my_text = input('Введите текст для архивирования (сжатия): ')
my_text_encode = txt_encoder(my_text)
with open('task24_encode.txt', 'w') as data:
    data.write(my_text_encode)
print(f'Сжатый текст -> {my_text_encode}')
my_text_decode = txt_decoder(my_text_encode)
with open('task24_decode.txt', 'w') as data:
    data.write(my_text_decode)
print(f'Восстановленный текст -> {my_text_decode}')
