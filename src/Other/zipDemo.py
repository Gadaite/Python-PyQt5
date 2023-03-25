import zipfile
import time
import threading
startTime = time.time()
flag = True
def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='C:/Users/Gadaite/Desktop', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime - startTime))
        global flag
        flag = False
    except Exception as e:
        print(e)


def do_main():
    zfile = zipfile.ZipFile("C:/Users/Gadaite\Desktop/【公开】front测试(20230321).zip", 'r')
    # 开始尝试
    for number in range(20230101, 19999999999):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()


if __name__ == '__main__':
    do_main()
