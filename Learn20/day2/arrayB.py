#__author:  bwzhang
#__date:    2018/6/6

#method1:use python list.sort()
li1 = [1,2,56,3,8,67,90,54,2]
list_copy = li1
li1.sort()
print(li1)

#method2:use python min()
li2 = []
li1_copy = list_copy
i = 0
while True:
    if 1 <= len(li1_copy):
        li1_copy_min = min(li1_copy)
        li2.append(li1_copy_min)
        li1_copy.remove(li1_copy_min)
        i+= 1
    else:
        break
print li2

#methon3: python --simple sort
li3 = [1,2,56,3,8,67,90,54,2]
li3_length = len(li3)
for i in range(li3_length):
    for j in range(i+1,li3_length):
        if li3[i] > li3[j]:
            handshark = li3[i]
            li3[i] = li3[j]
            li3[j] = handshark
print li3

#methon4: python---bubble sort
li4 = [1,2,56,3,8,67,90,54,2]
li4_length = len(li4)
for i in range(li4_length):
    j = li4_length - 2
    while j >= i:
        if li4[j] >li4[j+1]:
            handshark1 = li4[j]
            li4[j] = li4[j+1]
            li4[j+1] =handshark1
        j-=1
print li4

#methon5: python--shell sort (souxiaozengliang)
li5 = [1,2,56,3,8,67,90,54,2]
li5_length = len(li5)
increment = len(li5)
while increment > 1:
    increment = int(increment/3) + 1
    for i in range(increment+1,li5_length):
        if li5[i] < li5[i-increment]:
            handshark = li5[i]
            j = i - increment
            while j >= 0 and handshark < li5[j]:
                li5[j+increment] = li5[j]
                j -= increment
            li5[j+increment] = handshark
print li5
