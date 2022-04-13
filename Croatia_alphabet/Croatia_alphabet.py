#kro -> cro
def trim_kro(kro_str):
    count_str = len(kro_str)
    for i in range(len(kro_str)):
        if kro_str[i] == '=':
            if kro_str[i-1] == 'z' and kro_str[i-2] == 'd':
                count_str -= 2
            else:
                count_str -= 1
        elif kro_str[i] == '-':
            count_str -= 1
        elif kro_str[i] == 'j':
            if kro_str[i-1] == 'l' or kro_str[i-1] == 'n':
                count_str -= 1
    return count_str

ask = input('Write word: ')
print('length of word is:', trim_kro(ask))