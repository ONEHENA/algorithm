a, b, c = map(int, input().split())

# 두 수의 최대공약수(GCD) 계산
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 세 수의 최소공배수(LCM) 계산
def lcm_three(x, y, z):
    max_value = max(x, y, z)

    # 0이 입력된 경우 예외 처리
    if max_value == 0:
        return 0

    multiple = max_value

    while True:
        if multiple % x == 0 and multiple % y == 0 and multiple % z == 0:
            return multiple
        multiple += max_value

result = lcm_three(a, b, c)

print(result)
