import requests
def get_github_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")


        if response.status_code == 200:
            data = response.json()
            print(f"Name: {data['name']}")
            print(f"Repos: {data['public_repos']}")
        elif response.status_code == 400:
            print(f"Error: User '{username}' not found")
        else:
            print(f"Error: Status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error: Cant even afford internet haha")
# TEST
get_github_user("Effortlessss")
print()
get_github_user("FAKEUSERXYZ123")