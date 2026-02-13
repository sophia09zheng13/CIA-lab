def load_chinese_file(filename):
    # in the open command above, notice that we do not specify the encoding
    # that is because we are opening the file in *binary* mode
    # (the 'b' stands for binary, and the 'r' for read) 
    # files opened in binary mode return bytes objects
    # these need to be manually converted to strings using the .decode method
    f = open(filename, 'br')
    bs = f.read()
    try:
        text = bs.decode('gb2312')
        print('gb2312')
    except UnicodeDecodeError:
        text = bs.decode('big5')
        print('big5')
    return text
