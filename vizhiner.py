def input_func():
    #m = 26

    print("Введите текст на английском языке:")
    input_text = input().lower().replace(' ', '')
    input_text = delete_extra(input_text)

    while eng_alp(input_text) == False:
        print("Вы ввели текст не на английском. \nВведите текст на английском языке:")
        input_text = input().lower().replace(' ', '')
        input_text = delete_extra(input_text)

    print("Введите тип шифра:\n 1 - классический;\n 2 - самоключ;\n 3 - самоключ по шифротексту.")
    type = int(input())

    print("Введите необходимое действие de/en:")
    en_de = input().lower()

    if type == 1:
        print("Введите ключ:")
        slogan = input().lower()
        slogan = delete_extra(slogan)
        while eng_alp(slogan) == False:
            print("Вы ввели ключ не на английском. \nВведите ключ на английском языке:")
            slogan = input().lower()
            slogan = delete_extra(slogan)
    elif type == 2 or type == 3:
        print("Введите ключ:")
        slogan = input().lower()
        slogan = delete_extra(slogan)
        while len(slogan) != 1:
            print("Длинна ключа должна быть равна 1")
            slogan = input().lower()
            while eng_alp(slogan) == False:
                print("Вы ввели ключ не на английском. \nВведите ключ на английском языке:")
                slogan = input().lower()
                slogan = delete_extra(slogan)

    while en_de != "en" and en_de != "de":
        print("Некоректно введено необходимое действие, введите en либо de:")
        en_de = input().lower()

    if en_de == "en":
        print("Полученный закрытый текст:")
        print(encrypt(input_text, slogan, type))
    if en_de == "de":
        print("Полученный открытый текст:")
        print(decrypt(input_text, slogan, type))


def eng_alp(text: str) -> bool:
    for symbol in text:
        if 97 > ord(symbol) or ord(symbol) > 123:
            return False
    return True

def delete_extra(open_text: str) -> str:
    for x in "1234567890-=`<>,.":
        open_text.replace(x, '')
    return open_text

def gamma_forming_encrypt(open_text: str, slogan: str, type: int) -> str:
    if type == 1:
        return slogan*(len(open_text) // len(slogan) + 1*int(bool(len(open_text)%len(slogan))))
    if type == 2:
        return slogan + open_text[0:len(open_text)-1]
    if type == 3:
        for i in range(len(open_text)-1):
            slogan += chr((ord(slogan[i])+ord(open_text[i])- 97*2)%26 + 97)
        #print(slogan)
        return slogan

def encrypt(open_text: str, slogan: str, type: int) -> str:
    gamma = gamma_forming_encrypt(open_text, slogan, type)
    #print(gamma)
    close_text = ''
    for i in range(len(open_text)):
        close_text += chr(97 + (ord(open_text[i])-97 + ord(gamma[i])-97) % 26)
    return close_text

def gamma_forming_decrypt(close_text: str, slogan: str, type: int) -> str:
    if type == 1:
        return slogan*(len(close_text) // len(slogan) + 1*int(bool(len(close_text)%len(slogan))))
    if type == 2:
        for i in range(len(close_text)-1):
            slogan += chr(97+(ord(close_text[i])-ord(slogan[i]))%26)
        return slogan
    if type == 3:
        for i in range(len(close_text)-1):
            open_sym = chr(((ord(close_text[i])-97) - (ord(slogan[i]) - 97))%26 + 97)
            slogan += chr((ord(slogan[i])- 97 + ord(open_sym)-97)%26 + 97)
        #print(slogan)
        return slogan

def decrypt(close_text: str, slogan: str, type:int) -> str:
    open_text = ''
    gamma = gamma_forming_decrypt(close_text, slogan, type)
    for i in range(len(close_text)):
        open_text += chr(97 + (ord(close_text[i]) - ord(gamma[i])) % 26)
    return open_text

if __name__ == "__main__":
    input_func()