# Convert postfix to Prefix expression
def postToPre(post_exp):
    s = []
    operators = ['+', '-', '*', '/', '^']
    # length of expression
    length = len(post_exp)

    # reading from right to left
    for i in range(length):

        # check if symbol is operator
        if post_exp[i] in operators:

            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            # concat the operands and operator
            temp = post_exp[i] + op2 + op1

            # Push string temp back to stack
            s.append(temp)

        # if symbol is an operand
        else:

            # push the operand to the stack
            s.append(post_exp[i])
    print(s)
    ans = ""
    for i in s:
        ans += i
    return ans


# Driver Code
if __name__ == "__main__":
    post_exp = "AB+CD-*"

    # Function call
    print("Prefix : ", postToPre(post_exp))

