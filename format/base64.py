def convert_binary(data):
    s = str(data)
    binarys = []
    for i in s:
        b = bin(ord(i))
        binarys.append('{0:0>8s}'.format(b.replace('0b','')))
    return ''.join(binarys)
def encode_binary(binary):
    num = int(binary,2)
    if num == 62:
        return '+'
    elif num == 63:
        return '/'
    elif num <= 25:
        return chr(ord('A') + num)
    elif num <= 51:
        return chr(ord('a') + (num - 26))
    else:
        return str(num - 52)
    return '-'
def decode_char(char):
    if char == '+':
        return 62
    elif char == '/':
        return 63
    elif char >= 'A' and char <= 'Z':
        return ord(char)  -  ord('A')
    elif char >= 'a' and char <= 'z':
        return ord(char) - ord('A') - 6
    else:
        return int(char) + 52
def encode_string(data):
    binary_data = convert_binary(data)
    encode_string = ''
    for i in range(0,len(binary_data),6):
        binary = binary_data[i:i+6]
        if len(binary) != 6:
            binary += '0'*(6 - len(binary))
        encode_string += encode_binary(binary)
    if len(encode_string) % 4 != 0:
        encode_string += '=' * (4 - (len(encode_string) % 4))
    return encode_string
def encode_string_url_safe(string):
    return encode_string(string).replace('+','-').replace('/','_').replace('=','')

def decode_string(encode_data):
    decode_string = ''
    decode_binary = ''
    for c in encode_data:
        if c == '=':
            continue
        dc = decode_char(c)
        bdc = bin(int(dc)).replace('0b','')
        if len(bdc) != 6:
            bdc = '0' * (6 - len(bdc)) + bdc
        decode_binary += bdc
    for i in range(0,len(decode_binary),8):
        b = decode_binary[i:i+8]
        if len(b) != 8:
            continue
        decode_string += chr(int(b,2))
    return decode_string

src = 'AASEDRTewrfigkjuijewbfhiunjhbunj123456780[oipouhpiojnbhui'
dsrc = 'QUFTRURSVGV3cmZpZ2tqdWlqZXdiZmhpdW5qaGJ1bmoxMjM0NTY3ODBbb2lwb3VocGlvam5iaHVp'
cb = encode_string(src)
dc = decode_string(dsrc)

if cb == dsrc:
    print('encode ok!!!')
if dc == src:
    print('decode ok!!!!')
