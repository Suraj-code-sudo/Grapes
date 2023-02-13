# Problem
# 2022 is a year of the Winter Olympics! Curling has been one of the most popular winter sports as it requires skill, strategy, and sometimes a bit of luck.

# In a curling game, two teams compete by sliding heavy granite stones on a long ice sheet. We call the teams the red team and the yellow team, as their stones are usually distinguished by the red and the yellow handle color. A curling game consists of several ends (subgames); in every end, the teams, each owning 8 stones, take turns to slide them across the long ice sheet toward a circular target area called the house. A stone may hit existing stones to change its own moving direction and other stones' position (including knocking them out of play). Roughly speaking, the goal for a team is to make their stones as close to the center of the house as possible.

# Geometrically, a house and a stone can be modeled as a circle and a disk (the region bounded by a circle), respectively, and the scoring rules at the conclusion of each end are formally summarized as follows.

# Each stone can be viewed as a disk of radius Rs on a 2-dimensional plane.
# The house is a circle of radius Rh centered at (0,0).
# Only stones in the house are considered in the scoring. A stone is in the house if any portion of the stone lies on or within the circle representing the house. Tangency also counts.
# A team is awarded 1 point for each of their own stones in the house such that no opponent's stone is closer (in Euclidean distance) to the center than it. We assume in this problem that no two stones are equally close to the center (0,0).
# Two teams are playing and have just delivered all their stones. The red team has N stones remaining on the curling sheet, centered at (X1,Y1),(X2,Y2),…,(XN,YN), while the yellow team has M stones remaining, centered at (Z1,W1),(Z2,W2),…,(ZM,WM). Now you are asked to figure out the scores of both teams.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.

# Each test case begins with a line containing the two space-separated integers Rs and Rh.

# The next line contains the integer N. Then N lines follow, the i-th line of which containing the two space-separated integers Xi and Yi.

# After that, similarly, the next line contains the integer M. In the next M lines, the i-th line contains the two space-separated integers Zi and Wi.

# Output
# For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the score of the red team, and z is the score of the yellow team.

import math

for case in range(int(input())):
    rs, rh = map(int, input().split())
    red = int(input())
    score_red = 0
    score_yellow = 0

    red_dist = []
    yellow_dist = []
    min_red = 0
    min_yellow = 0

    for _ in range(red):
        x, y = map(int, input().split())
        x = abs(x)
        y = abs(y)
        if (x+y)-rs in range(-rh, rh+1):
            print("Red", math.sqrt(x**2 + y**2 ))
            red_dist.append(math.sqrt(x**2 + y**2 ))

    yellow = int(input())
    for _ in range(yellow):
        x, y = map(int, input().split())
        x = abs(x)
        y = abs(y)
        if (x+y)-rs in range(-rh, rh):
            yellow_dist.append(math.sqrt(x**2 + y**2 ))

    if yellow_dist: min_yellow = min(yellow_dist)
    if red_dist: min_red = min(red_dist) 

    print(min_red, min_yellow)

    if min_red == 0: print(f"Case #{case+1}: ",score_red, len(yellow_dist))
    elif min_yellow == 0: print(f"Case #{case+1}: ",len(red_dist), score_yellow)
    else:
        for dist in red_dist:
            if min_yellow > dist:
                score_red += 1
        for dist in yellow_dist:
            if min_red > dist:
                score_yellow += 1
            
        print(f"Case #{case+1}: ",score_red, score_yellow)