# for only 2 integer case

var1 = input('Enter 1st Number in a String: ')
var2 = input('Enter 2nd Number in a String: ')

sum = 0

def straddNumbers(a, b):
    print("Your First Number is" ,a, "and Type is", type(a))
    print("Your Second Number is" ,b, "and Type is", type(b))
    
    newVar = float(a) + float(b)
    
    return newVar
    
sum = straddNumbers(var1, var2)
print('the sum of the numbers is : ', sum);
input()
