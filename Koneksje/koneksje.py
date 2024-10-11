from collections import defaultdict, deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    direct_connections = set(graph[start])  # Store direct connections

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return direct_connections

def solve_koneksje():
    # Read input
    s, k = map(int, input().split())
    
    # Create graph
    graph = defaultdict(set)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    # Process queries
    n = int(input())
    for _ in range(n):
        s1, s2 = map(int, input().split())
        direct_connections = bfs(graph, s1)
        if s2 in direct_connections:
            print("TAK")
        else:
            print("NIE")

if __name__ == "__main__":
    solve_koneksje()