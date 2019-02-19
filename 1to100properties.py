x=input("input x from 1-100:")
try:
    x=int(x)
except:
    x=-1
if x>0 and x<10:
    print("one digit")
    print("Range:1s")
elif x<100:
    print("double digits")
    if x>=10 and x<20:
        print("Range:10s")
    elif x<30:
        print("Range:20s")
    elif x<40:
        print("Range:30s")
    elif x<50:
        print("Range:40s")
    elif x<60:
        print("Range:50s")
    elif x<70:
        print("Range:60s")
    elif x<80:
        print("Range:70s")
    elif x<90:
        print("Range:80s")
    elif x<100:
        print("Range:90s")
elif x==100:
    print("Triple digits")
    print("Range:100s")
elif x==0 or x>100 or x<-1:
    print("Out of range")
elif x==-1:
    print("Not a number")
print("All done")
