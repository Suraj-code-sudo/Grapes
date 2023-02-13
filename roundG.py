# Problem
# John participates in an annual walking competition called Walktober. The competition runs for a total of N days and tracks the daily steps of the participants for all the N days. Each participant will be assigned a unique ID ranging from 1 to M where M is the total number of registered participants. A global scoreboard is maintained tracking the daily steps of each participant.

# John is determined to win Walktober this year and his goal is to score the maximum daily steps on each of the N days among all the participants. Having participated in Walktober last year as well, he wanted to know how many steps he fell short of in achieving his goal. Given the previous year scoreboard, calculate the minimum additional steps he needed over his last year score in order to achieve his goal of scoring the maximum daily steps every day.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# The first line of each test case contains three integers M, N, and P denoting the total number of participants, the total number of days the competition runs, and the last year participant ID of John.
# The next M lines describe the scoreboard of the previous year and contains N integers each. The j-th integer of the i-th line denotes the step count Si,j of the participant with ID i on the j-th day of the competition.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum total additional steps needed by John to achieve his goal.


for case in range(int(input())):
    m, n, p = map(int, input().split())
    p-=1
    array = []
    for _ in range(m):
        row = list(map(int, input().split()))
        array.append(row)
    max_array = []
    result = 0
    for j in range(n):
        max_ = 0
        for i in range(m):
            if max_ < array[i][j]:max_=array[i][j]
        max_array.append(max_)

    for k in range(n):
        if array[p][k] < max_array[k]:result+=(max_array[k]-array[p][k])
    print(f"Case #{case+1}: ",result)