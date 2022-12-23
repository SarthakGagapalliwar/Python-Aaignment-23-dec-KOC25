sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l1=sample_list[0:len(sample_list)//3]
l2=sample_list[len(sample_list)//3:2*len(sample_list)//3]
l3=sample_list[2*len(sample_list)//3:len(sample_list)]
print("chunk  1",l1)
print("after reversing it ",l1[::-1])
print("chunk  2 ",l2)
print("After reversing it ",l2[::-1])
print("chunk 3 ",l3)
print("after reversing it ",l3[::-1])