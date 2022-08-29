class MyException(Exception):
    def __int__(self):
        print('Имя не может содержать в себе цифры')


def check_name(name):
    for i in range(10):
        if str(i) in name:
            raise MyException
    print(name)