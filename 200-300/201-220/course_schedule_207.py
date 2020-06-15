# graph - dfs

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        def get_adjacency_list(edges, N):
            adjacency_list = [[] for _ in range(N)]
            for edge in edges:
                adjacency_list[edge[1]].append(edge[0])
            return adjacency_list
        
        def is_cyclic(adjacency_list, N):
            visited = [False] * N
            current_element_stack = [False] * N
            for i in range(N):
                if not visited[i]:
                    if dfs(i, adjacency_list, visited, current_element_stack):
                        return True
            return False
                        
        def dfs(i, adj, visited, current_element_stack):
            visited[i] = True
            current_element_stack[i] = True
            for j in range(len(adj[i])):
                if current_element_stack[adj[i][j]]:
                    return True
                if not visited[adj[i][j]]:
                    if dfs(adj[i][j], adj, visited, current_element_stack):
                        return True
            current_element_stack[i] = False
            return False
        
        adjacency_list = get_adjacency_list(prerequisites, numCourses)
        return not is_cyclic(adjacency_list, numCourses)
        
