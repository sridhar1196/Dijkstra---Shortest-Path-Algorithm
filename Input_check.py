import fileinput
import sys
n = len(sys.argv)
#for i in range(2,n):
#    print (sys.argv[i])
fileName = input("Enter file name:")

q = True
while(q):
    temp = input()
    if temp=="q":
        q = False