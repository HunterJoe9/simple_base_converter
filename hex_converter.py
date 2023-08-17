# base10_Converter11

# def = 함수 선언
def converter(n,m):
    result = []
    #while loop 
    while True:
        # n / m == 0이라면 실행
        if n // m == 0:
            result.append(n) # 마지막 나머지
            break
        result.append(n%m) #나머지 result list에 저장 
        n = n // m #나눈 몫
    result.reverse() # list 뒤집기 
    return int("".join(map(str, result)))

n = int(input("which num? : "))
m = int(input("what based? : "))

base10_converter = converter(n,m)
print(base10_converter)









