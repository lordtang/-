import os
def isEnd():
    str = ''
    i = 0
    f = open('data.csv',encoding='utf-8')
    while True:
        data = f.read(10)
        if data == '':
            print('end')
            break
        else:
            print(i)
            i+=1
if __name__ == '__main__':
    isEnd()