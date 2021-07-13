n = int(input())
student_marks = {}                           # creating dictionary
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))          # creating list of scores
    student_marks[name] = scores             # getting name and scores in dictionary
query_name = input()
query_score=student_marks[query_name]        # getting query_name's value
average= sum(query_score)/len(query_score)   # forrmula for finding average
print('%.2f'%average)                        # %.2f is used to print average with two decimal places
