"""
Exercise 2: Browser History
File: 02_browser_history.py

Rules:
1. Create a list called 'history' with 5 website URLs (e.g., "google.com", "github.com", etc.).
2. The list represents the order of visited sites (the first item is the oldest, the last item is the newest).
3. Print the oldest site visited using index 0.
4. Print the most recently visited site using the correct negative index.
5. The user clicked the "Back" button. Print the second most recently visited site using a negative index.
"""

history = ["github.com","youtube.com","gemini.google.com/app","primevideo.com","amazon.com.br"]
print(f"Acess history: {history}")
oldest_site_visited = history[0]
print(f"Oldest site acessed: {oldest_site_visited}")
newest_site_visited = history[-1]
print(f"Newest site acessed: {newest_site_visited}")
second_most_recently_visited_site = history[-2]
print(f"Second most recently visited: {second_most_recently_visited_site}")