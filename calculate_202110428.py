# Calculations in reverse Polish notation
def calculate():
    code =[]
    endnumflg = 0
    endopflg = 0
    while(endnumflg == 0):
        enternum = input("Enter integers... (if you finish input integer, input 'end') ")
        if(enternum == 'end'):
            endnumflg = 1
            break
        code.append(int(enternum))
        print("Current code is {}".format(code))
        
    while(endopflg == 0):
        enterop = input("Enter operation... (if you finish input operation, input 'end') ")
        if(enterop == 'end'):
            endopflg = 1
            break
        code.append(enterop)
        print("Current code is {}".format(code))
        
    stack = []
    print(" ")
    print("Input code is {}".format(code))
    print("Start Calculate...")
    while len(code) > 0:
        op = code.pop(0)
        if op == "+":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
            print("calculate {} + {} ...".format(n2, n1))
        elif op == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
            print("calculate {} - {} ...".format(n2, n1))
        elif op == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
            print("calculate {} * {} ...".format(n2, n1))
        elif op == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 // n1)
            print("calculate {} // {} ...".format(n2, n1))
        else:
            stack.append(op)
    ans = stack[-1]
    print("The Answer is {} !".format(ans))

calculate()
#calculate([3,10,4,1, "-", "/", "+"]) *answer is 6