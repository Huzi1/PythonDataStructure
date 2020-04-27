# class Factorial():

#     def __init__(self,num):
#         self.num = num

def factorial(num):
    if(num==1):
        print(num)

        return 1
    else:
        # recursive call
        print(num)
        returnNum = num * factorial(num-1) 
        # 
        return returnNum  

def main(num):
    print(type(num))
    num = int(num)
    if (num<0 ):
        print("negative, no factorial")
    elif(num == 0):
        print("1")
    else:
        print("The factorial of", num, "is", factorial(num))        




main(4)