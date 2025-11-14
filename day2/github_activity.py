# Your commits this week
commits = [
    "Built Calculator",
    "Made billing system",
    "Started GitHub logger",
    "Fixed login bug"
]
# print total
print(f"Total commits this week: {len(commits)}")
# print each one
print("\n This week's work:")
for i, commit in enumerate(commits,1):
    print(f"  {i}. {commit}")
# add todays work 
today = input("\n What did you build today?")
commits.append(today)
print()
print(f"Updated total: already {len(commits)} commits! Fuck yeah!!! ")
   