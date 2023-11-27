'''
피제수(분자) A와 제수(분모) B가 있다. 
두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다. 
예를 들어, A=3, B=4, N=1이라면, A÷B=0.75 이므로 출력 값은 7이 된다.

첫 번째 줄에 A와 B(1 ≤ A, B ≤ 100,000), N(1 ≤ N ≤ 1,000,000)이 공백을 경계로 주어진다.

A÷B를 했을 때, 소숫점 아래 N번째 수를 출력한다.
'''
import sys

A, B, N=map(int,sys.stdin.readline().split())

for i in range(N) :
    A = (A%B)*10
    result = A//B
 
print(result)

# print(math.floor((A/B)*(10**N)%10))
# OverflowError
# OverflowError는 산술 연산의 결과가 표현하기에는 너무 클 때 발생하는 에러입니다. 
# Python은 정수 크기의 제한이 없기 때문에, 이 에러가 발생하지 않습니다. 
# 하지만, 정수에서도 요구하는 범위를 벗어나는 것과 같은 일부 경우에 발생할 수도 있습니다.
