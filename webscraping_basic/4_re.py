import re

# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") 

def print_match(m):
  if m:
    print("m.group(): ", m.group())   # 일치하는 문자열 반환
    print("m.string: ", m.string)     # 입력받은 문자열
    print("m.start(): ", m.start())     # 일치하는 문자열의 시작 인덱스
    print("m.end(): ", m.end())       # 일치하는 문자열의 끝 인덱스
    print("m.span(): ", m.span())     # 일치하는 문자열의 시작과 끝 인덱스를 함께
  else:
    print("매칭되지 않음")

# m = p.match("careless")   # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care")   # search: 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m)

# lst = p.findall("careless")     # findall: 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# lst = p.findall("good care")     
# print(lst)

# lst = p.findall("good care cafe")     
# print(lst)


# 1.    p = re.compile("원하는 형태")
# 2.    m = p.match("비교할 문자열")      : 주어진 문자열의 처음부터 일치하는지 확인
#       m = p.search("비교할 문자열")     : 주어진 문자열 중에 일치하는 게 있는지 확인
#       lst = p.findall("비교할 문자열")  : 일치하는 모든 것을 리스트 형태로 반환
