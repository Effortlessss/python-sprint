# commit_tracker.py
# A single commit with ALL its info 

commit = {
    "date": "2025-11-14",
    "repo": "python-sprint",
    "message": "Finally start and take action now just keep it up",
    "lines_added": 100,
    "language": "Python"
}

# acces specific data
print(f"Date: {commit['date']}")
print(f"Repo: {commit['repo']}")
print(f"What you did: {commit['message']}")
print(f"Lines added: {commit['lines_added']}")

# Add new info
commit["time_spent"] = "180 minutes"
commit["bugs_found"] = 5

print(f"\n Time spent: {commit['time_spent']}")
print(f" Bugs found: {commit['bugs_found']}")

# Now we will make it a list
commits = [commit]

# Calculate total
total_lines = sum(c['lines_added'] for c in commits)
print(f"\n TOTAL LINES: {total_lines}")
