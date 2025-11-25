def main():
    xx=int(input())
    list_a=[]
    list_b=[]
    i = 1
    while i<=xx//2+1:
        sum_ = i
        j=i+1
        while sum_<xx:
            sum_+=j
            j+=1
        if sum_==xx:
            list_a.append(i)
            list_b.append(j-1)
        i+=1

    for i in range(len(list_a)):
        print(list_a[i], list_b[i])
if __name__ == '__main__':
    main()