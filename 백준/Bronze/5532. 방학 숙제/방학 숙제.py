l = int(input())
a = int(input()) # 국어 총 페이지
b = int(input()) #수학 총 페이지
c = int(input()) # 국어 하루 총 가능페이지
d = int(input()) # 수학 하루 총 가능페이지

kor_n = a%c
kor = a//c
mat_n =b%d
mat = b//d
if kor_n!=0:
    kor+=1
if mat_n!=0:
    mat+=1

print(l-max(kor,mat))



