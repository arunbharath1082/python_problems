# Important
def happyNumber(n):
    slow=square_of_separteNum(n)

    fast=square_of_separteNum(square_of_separteNum(n))
    print(fast)
    while slow!=fast:
        slow=square_of_separteNum(slow)
        fast=square_of_separteNum(square_of_separteNum(fast))
    if slow==1:
        print("happy number is  present")
    else:
        print("happy number is  not present")


def square_of_separteNum(n):
    ans=0
    while n>0:
        temp=n%10
        ans+=temp**2
        n=n//10

    return ans



if __name__=='__main__':
    happyNumber(19)