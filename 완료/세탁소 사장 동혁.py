n = int(input())

for i in range(n):
	change = int(input())
	for i in [25, 10, 5, 1]:
		print(change//i, end=' ')
		change = change%i

# T = int(input())

# for i in range(T) :
#     change = int(input())
#     while change > 0 :
#         Q = change//25
#         change = change%25

#         D = change//10
#         change = change%10

#         N = change//5
#         change = change%5  

#         P = change//1
#         change = change%1   
        
#         print(Q,D,N,P, end=" ")
#     print()

