'''
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다.
단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 
또한 문자열은 공백으로 시작하거나 끝날 수 있다.
'''
# The Curious Case of Benjamin Button

#1 input()을 사용한 version -> 소량의 입력값을 처리
a = input().strip().split(' ')
if a == [' ']:
    print(0)
else :
    print(len(a))

#1 sys.stdin.readline()을 사용한 version -> 대량의 입력값을 빠르게 처리 가능
import sys
s = sys.stdin.readline().strip()
s = s.split(' ')
if s == ['']:
    print(0)
else:
    print(len(s))