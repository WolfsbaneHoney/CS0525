def movingaverage(list, n) :
    result = []
    for i in range(len(list)):
        if i < n-1:
            #uso lo slicing [ da : a] per creare sottogruppi
            average = sum(list [:i +1]) / (i+1)
        else: 
            average = sum(list [i-n+1 :i+1]) / n
        result.append(average)
    return result

nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

num = input("Di quanti numeri vuoi la media mobile? ")

print(movingaverage(nlist, int(num)))