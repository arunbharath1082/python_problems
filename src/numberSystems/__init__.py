import math


def number_of_digits(n):

    # first method
    # count=0
    # while n>0:
    #     n=n//10
    #     count+=1
    # return count

    # second method
    return math.ceil(math.log10(n))




if __name__ == "__main__":
    print(number_of_digits(12345))