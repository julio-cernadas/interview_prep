from collections import defaultdict


def accounts_merge(accounts):
    # Step 1: Create a dictionary to map each email to a name
    email_to_name = {}

    # Step 2: Create a graph to represent the connections between emails
    graph = defaultdict(list)

    # Step 3: Build the email_to_name dictionary and graph
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name
            graph[account[1]].append(email)
            graph[email].append(account[1])

    visited = set()
    result = []

    # Step 4: Traverse the graph using depth-first search (DFS)
    def dfs(node, emails):
        if node in visited:
            return
        visited.add(node)
        emails.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, emails)

    # Step 5: Iterate through each email and perform DFS to find connected emails
    for email in graph:
        if email not in visited:
            email_list = []
            dfs(email, email_list)
            result.append([email_to_name[email]] + sorted(email_list))

    return result


data = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"],
]
merged_accounts = accounts_merge(data)
print(merged_accounts)
