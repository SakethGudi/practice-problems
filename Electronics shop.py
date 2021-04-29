def getMoneySpent(keyboards, drives, b):
    money=[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if(keyboards[i]+drives[j]<=b):
                money.append(keyboards[i]+drives[j])
            else:
                money.append(-1)
    k=max(money)
    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
