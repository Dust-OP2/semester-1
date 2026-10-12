"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }


systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
while systime <= maxtime:
    for i in states:
        state = i
        for j in range (states[i]):
            if systime <= maxtime:
                print(f"Time {systime:03} State {state}")
                systime += 1
            else:
                break




# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14