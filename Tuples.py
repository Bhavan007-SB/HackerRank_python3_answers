n = int(input())
integer_list = map(int, input().split())
t = hash(tuple(integer_list))
print(t)
