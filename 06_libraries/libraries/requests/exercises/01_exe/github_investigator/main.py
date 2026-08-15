"""
Python Core - 06 Libraries (requests)
Exercise 2: The GitHub Repository Investigator (Intermediate - Logic & Interpretation)
Folder: 02_github_investigator/
Main File: main.py

Rules:
1. Create a function named 'fetch_user_repositories(username: str)'.
2. Inside the function, define the GitHub API target URL:
   f"https://api.github.com/users/{username}/repos"
3. Create a dictionary for query parameters to sort the repositories by latest updates and limit the results:
   query_params = {"sort": "updated", "per_page": 10}
4. Use a 'try/except' block to make the GET request, passing the 'params' argument and setting a 'timeout=5'.
5. Inside the 'try' block, call 'response.raise_for_status()' to catch HTTP errors.
6. If an HTTPError happens (e.g., Error 404 for a user that doesn't exist), catch it in the except block, print:
   "[ERROR] User not found on GitHub." and return an empty list [].
7. If the request succeeds, parse the JSON response (it will be a list of dictionaries, each representing a repository).
8. Find and print the repository with the highest number of stars ('stargazers_count'). Show its:
   - Name ('name')
   - Description ('description')
   - Star count ('stargazers_count')
9. Test your function at the bottom of the file with a valid user like 'fetch_user_repositories("torvalds")' 
   and an invalid one like 'fetch_user_repositories("non_existent_user_999999")'.
"""

import requests

def search_repositories(usuario: str):
   url = f"https://api.github.com/users/{usuario}/repos"
   query_params = {"sort": "updated", "per_page": 10}
   try:
      response = requests.get(url, params=query_params, timeout=5)
      response.raise_for_status()
      repositories = response.json()
      if repositories == []:
                 return
      list_of_repos = []
      more_stars_repo = repositories[0]
      stars = repositories[0]['stargazers_count']
      for rep in repositories:
            list_of_repos.append(rep)
            if rep['stargazers_count'] > stars:
                 stars = rep['stargazers_count']
                 more_stars_repo = rep
      print(f"--- Repository With More Stars [USER: {usuario}] ---\n"
            f"\Repository name: {more_stars_repo['name']}\n"
            f"Repository description: {more_stars_repo['description']}\n"
            f"Repository star count: {more_stars_repo['stargazers_count']}\n")
      
   except requests.exceptions.HTTPError as err_http:
        print(f"[ERROR] User not found on GitHub: {err_http}")
        return []
   except requests.exceptions.Timeout:
        print("[TIMEOUT] The server took too long to respond!")
   except requests.exceptions.ConnectionError:
        print("[CONNECTION ERROR] No internet connection or server is completely offline.")
   except Exception as e:
        print(f"[CRITICAL] An unexpected error occurred: {e}")

search_repositories("octocat")
search_repositories("torvalds")