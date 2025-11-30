import requests
def get_github_stats(username):
    try:
           
        # API CALL 1: Get user info
        user_response = requests.get(f"https://api.github.com/users/{username}")
        user_data = user_response.json()

        # API CALL 2: Get repos
        repos_response = requests.get(f"https://api.github.com/users/{username}/repos")
        repos = repos_response.json()

        # NOW YOU HAVE BOTH - combine the data so extract everything
        name = user_data["name"]
        followers = user_data["followers"]
        total_repos = len(repos) # len counts repos for you 

        # Now we calculate total stars
        total_stars = 0
        for repo in repos:
            total_stars += repo["stargazers_count"]
        
        # Print Dashboard
        print("GITHUB STATS")
        print(f"Name: {name}")
        print(f"Followers: {followers}")
        print(f"Total Repos: {total_repos}")
        print(f"Total Stars: {total_stars}")
         
    except requests.exceptions.ConnectionError:
        print("Error: No internet")
    except KeyError:
        print("Error: Invalid data format")   

get_github_stats("Effortlessss")
