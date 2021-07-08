n = int(input())
arr = map(int, input().split())
lst=list(arr)
score = sorted(lst)
for i in score:
    for j in score:
       if score[-1] == score[-2]:
          score.remove(score[-1])
score.remove(max(score))
print(max(score))
