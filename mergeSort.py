def mergeSort(num):
    if len(num) > 1:
        temp = len(num)//2
        LFT = num[:temp]
        RGT = num[temp:]

        mergeSort(LFT)
        mergeSort(RGT)

        x = y = z = 0
        
        while x < len(LFT) and j < len(RGT):
            if LFT[x] < RGT[y]:
                num[z] = LFT[x]
                x += 1
            else:
                num[z] = RGT[y]
                y += 1
            z += 1

num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
print(num)