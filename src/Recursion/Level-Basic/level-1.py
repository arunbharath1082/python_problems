
def number(n):
    if n>0:
        number(n-1)
        print(n)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
def reverse(n):
    if n==0:
        return
    print(n%10,end="")
    reverse(n//10)
def reversesum(n):
    if n==0:
        return 0
    return (n%10)*10**(len(str(n))-1)+reversesum(n//10)
def palindrome(n):
    if n==reversesum(n):
        return True
    return False

def countZeros(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+countZeros(n//10)
    return countZeros(n//10)


if __name__ == "__main__":
    # number(5)
    # print(factorial(5))
    # print(sumofdigits(12345))
    # print(power(2,5))
    # reverse(12345)
    print(countZeros(1020304050))