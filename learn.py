from duckduckgo_search import DDGS
def search_geeksforgeeks(query):
    search_query = f"{query} site:geeksforgeeks.org"

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(search_query, max_results=5):  # Fetch 5 results
            results.append((r["title"], r["href"]))

    return results

def learn():
    query = input("Enter the topic you want to search: ")
    docs = search_geeksforgeeks(query)
    if docs:
        print("\nTop Documentation Links from GeeksforGeeks:")
        for title, link in docs:
            print(f"- {title}: {link}")
    else:
        print("No results found.")

# query = input("Enter the topic you want to search: ")
# docs = search_geeksforgeeks(query)
# if docs:
#     print("\nTop Documentation Links from GeeksforGeeks:")
#     for title, link in docs:
#         print(f"- {title}: {link}")
# else:
#     print("No results found.")