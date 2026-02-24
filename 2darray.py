# 14/01/26
# S Krishna
# Basic demo of a 2D array
# Data captures network activity over a week from 6am - 12pm

# STEP 1: setting up data
stats = [[0,0,0,8,11,9,15],                     # Sun
        [18,20,97,346,475,433,293],             # Mon
        [11,8,63,349,411,522,239],              # Tue
        [20,29,89,465,532,529,301],             # Wed
        [17,36,96,501,599,0,0],                 # Thu
        [0,0,0,0,6,3,0],                        # Fri
        [0,0,0,0,1,6,12]                        # Sat
    ]

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
houres = ["6", "7", "8", "9", "10", "11", "12"]

# STEP 2: Print the array
print(stats)

# STEP 3: Print it as a matrix
for row in range(7):             # Go through each day
    for col in range(7):         # Go through each hour
        print(stats[row][col], end=" ")
    print()

# STEP 4: Find busiest single time (day + hour)
maxDay = 0
maxTime = 0

for day in range(7):
    for time in range(7):
        if stats[day][time] > stats[maxDay][maxTime]:
            maxDay = day
            maxTime = time

print("Busiest single time was on", days[maxDay], "at", houres[maxTime])

# --------------------------------------------------
# QUESTION 1: Day of the week with highest total users
# --------------------------------------------------

maxTotal = 0
maxDay = 0

for day in range(7):
    rowTotal = 0
    for time in range(7):
        rowTotal += stats[day][time]

    if rowTotal > maxTotal:
        maxTotal = rowTotal
        maxDay = day

print("Day with highest total users:", days[maxDay])

# QUESTION 2: Busiest hour of the entire data


maxHourTotal = 0
maxHour = 0

for hour in range(7):
    colTotal = 0
    for day in range(7):
        colTotal += stats[day][hour]

    if colTotal > maxHourTotal:
        maxHourTotal = colTotal
        maxHour = hour

print("Busiest hour overall:", houres[maxHour])
















