def function1():
    print("This is ENG1003's first Tuturial Programing Task \nEnter the fuction to be excute:")
    print("YAN\nHim\nIan\nWalton\nRonald")
    
    
def function2():
    print('This text represent the content of function 2')  #To be edited by member 2, Replace this line with your actual function code
    a = int(input('please enter the first number'))
    b = int(input('please enter the second number'))
    c = int(input('please enter the third number'))

    sum=float(a) + float(b)+ float(c)

    print('a={0} b={1} c={2} ,the sum of them is {3}'.format(a,b,c,sum))



def function3():
    a = 5 
    print('a = '+str(a)+' , Square of a:  '+str(a*a))

def function4():
    x = 6 
    y = 4
    print('a = '+str(x)+' b = '+str(y))
    if x>y:
        print('a is larger than b')
    else:
        print('b is larger than a')  #To be edited by member 4, Replace this line with your actual function code


#The Main function edited by Group leader
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)
