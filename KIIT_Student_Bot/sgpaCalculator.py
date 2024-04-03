def get_sgpa(args):
    sum = 0
    creditSum = 0
    length = len(args)
    for i in range(0, length, 2):
        sum = sum + int(args[i]) * int(args[i+1])
        creditSum = creditSum + int(args[i+1])

    return sum/creditSum

