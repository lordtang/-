# coding = utf-8

def clear_blank_line():
    file1 = open('data.csv','r',encoding='utf8')
    file2 = open('data_new.csv','w',encoding= 'utf8')
    for line in file1:
        if line == '\n':
            pass
        else:
            file2.write(line)
    file1.close()
    file2.close()
if __name__ == '__main__':
    clear_blank_line()