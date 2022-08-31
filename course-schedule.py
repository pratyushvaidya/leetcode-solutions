# 207. COURSE SCHEDULE

class Solution:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    
    Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        topological_sorted_order = []
        is_possible = True
        
        color = {k: 1 for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            
            color[node] = 2
            
            if node in adj_list:
                for neighbour in adj_list[node]:
                    if color[neighbour] == 1: dfs(neighbour)
                    elif color[neighbour] == 2: is_possible = False
            color[node] = 3
            topological_sorted_order.append(node)
        
        for node in range(numCourses):
            if color[node] == 1: dfs(node)
        
        return is_possible
