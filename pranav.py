n = int(input())
sum1=0
l=[]
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

lis = student_marks[input()]
print(sum(lis)/len(lis))

"""
for i in student_marks:
    if i==query_name:
        l=student_marks[i]
        for j in l:
            sum1=sum1+j
t=sum1/len(scores)
print("{:.2f}".format(t))
"""