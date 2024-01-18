import sys

n = int(input())
for i in range(n) : 
    a,b = map(int,sys.stdin.readline().split( ))    
    total = a+b
    print(f"Case#{i}: {total}")

