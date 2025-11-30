import requests

def get_user_repos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")


    if response.status_code == 200:
        repos = response.json() # This is a LIST of dictionaries

        print(f"REPOS FOR {username}:")
        print("-" * 40)


        for repo in repos:
            print(f"Name: {repo['name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print("-" * 40)

    else:
        print(f"Error: {response.status_code}")

get_user_repos("Effortlessss")
