def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def PostToInfix(exp):
    s = []

    for i in exp:

        # Push operands
        if (isOperand(i)):
            s.append(i)

        # We assume that input is a
        # valid postfix and expect
        # an operator.
        else:

            op2 = s[-1]
            s.pop()
            op1 = s[-1]
            s.pop()
            s.append( "(" + op1 + i +
                     op2 + ")")

        # There must be a single element in
    # stack now which is the required
    # infix.
    return s[-1]


# Driver Code
if __name__ == '__main__':
    exp = "ab*c+"
    print(PostToInfix(exp))
