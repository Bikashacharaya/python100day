terms = int(input("enter the number of terms"))
n1,n2=0,1
count = 0
if terms<=0:
    print("enter the positive integer")
elif terms==1:
    print(n1)
else:
    print(f"the fabbinoci series upto {terms}th term is:")
    while terms>count:
        print(n1)
        nth = n1 + n2
        n1=n2
        n2 = nth
        count+=1

