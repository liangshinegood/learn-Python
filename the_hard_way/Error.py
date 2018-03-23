import  sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
#
# except OSError as err:
#     print("OS error:{0}".format(err))
# except ValueError:
#     print("Could not convert data to an inter")
# except:
#     print("Unexcept error:",sys.exc_info()[0])
#     raise
# else:
#     print("lalallallal")
#     f.close()


# def this_fail():
#     x = 1/0
# try:
#     this_fail()
# except ZeroDivisionError as err:
#     print('Handling run-time error:',err)
#
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# class MyError(Exception):
#     def __init__(self,value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occured,value:',e.value)

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye,world!')

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is",result)
    # finally:
    #     print("executing finally clause")

print(divide(2,1))

print(divide(2,0))

print(divide('2','1'))





