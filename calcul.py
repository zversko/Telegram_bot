import re

def calculator(s_new):
    # s_new = str(s_new)
    for i in range(3):
        if s_new.find(' * (-1)^0.5') != -1:
            s_new = s_new.replace(' * (-1)^0.5', 'j')
        elif s_new.find(' / (-1)^0.5') != -1:
            s_new = s_new.replace(' / (-1)^0.5', '/1j')
        else:
            s_new = s_new.replace('(-1)^0.5', '1j')
    s_new = s_new.replace(' ', '')
    if re.match(r'''[\d|j|\+|\-|\/|\*|\^]+''', s_new):
        s_new = str(eval(s_new))
    else:
        s_new = 'в выражении недопустимые символы'
    return s_new
    # result = str(complex(4+1j-1+8j-4/1j))
    # if result.find('+0j') != -1:
    #     result = result.replace('+0j', '')
    # elif result.find('-0j') != -1:
    #     result = result.replace('-0j', '')
    # result = result.replace('j', '(-1)^0.5')
    # result = result.replace('(', '')
    # result = result.replace(')', '')
    # return result

def main(message):
    # message = '4 + (-1)^0.5 - 1 + 8 * (-1)^0.5 - 4 / (-1)^0.5'
    # # print(f'{message} \n')
    res = complex(calculator(message))
    # print(res)

# main()