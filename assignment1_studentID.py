"""
Author: <Ariana Cruz>
Assignment: #1
"""

# Step b: Create 4 variables

# string
gym_member = "Ariana Cruz"

# float
preferred_weight_kg = 20.5

# integer
highest_reps = 25

# boolean


# Step c: Create a dictionary named workout_stats

workout_stats = {
    "Ariana": (30, 45, 20),
    "Jamie": (40, 30, 35),
    "Taylor": (50, 20, 25)
}

print("Dictionary created!")


# Step d: Calculate total workout minutes using a loop and add to dictionary

for friend, minutes in list(workout_stats.items()):
    total = sum(minutes)
    workout_stats[friend + "_Total"] = total

# Step e: Create a 2D nested list called workout_list

friends = [name for name in workout_stats if "_Total" not in name]

workout_list = [list(workout_stats[friend]) for friend in friends]

# Step f: Slice the workout_list

# Yoga and running for all friends
for i, friend in enumerate(friends):
    print(friend, workout_list[i][0:2])

# Weightlifting for last two friends
for i in range(len(friends) - 2, len(friends)):
    print(friends[i], workout_list[i][2])

# Step g: Check if any friend's total >= 120

for friend in friends:
    total = workout_stats[friend + "_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend

name = input("Enter a friend's name: ").strip()

if name in workout_stats and isinstance(workout_stats[name], tuple):
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[name + "_Total"]

    print("Yoga:", yoga)
    print("Running:", running)
    print("Weightlifting:", weightlifting)
    print("Total:", total)
else:
    print(f"Friend {name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend: workout_stats[friend + "_Total"] for friend in friends}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("Highest total:", highest, totals[highest])
print("Lowest total:", lowest, totals[lowest])