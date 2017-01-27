#open and read input file
with open("Input", "r") as f:
    text = f.read()
#generate binary numbers with encryption
def generate():
    gResult =[str('{0:b}'.format(ord(i))).zfill(8) for i in text]
    # {}.format() replace % in C
    gResult = ''.join(gResult)
    gResult = gResult.replace('11111','111110')
    with open("ASCII_codes","w") as f:
        f.write(gResult)
    return gResult
def recovery(string):
    string = string.replace('111110', '11111')
    string = [string[x:x+8] for x in range(0,len(string),8)]
    string = [chr(int(''.join(i),2)) for i in string]
    # print(string)
    string = ''.join(string)
    with open("Output","w") as f:
        f.write(string)

if __name__ == '__main__':
    # 只在本模块被调用时运行
    generate()
    recovery(generate())

