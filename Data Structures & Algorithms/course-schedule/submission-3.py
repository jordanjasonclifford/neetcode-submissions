class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list:
        # course -> list of prerequisites
        pre = defaultdict(list)
        for course, p in prerequisites:
            pre[course].append(p)
        
        # visited = courses we've fully processed (no cycles from them)
        visited = set()

        # path = current recursion stack (used to detect cycles)
        path = set()

        def dfs(course):
            # If course is in current path → cycle detected
            if course in path:
                return False
            
            # If already processed before → it's safe
            if course in visited:
                return True
            
            # Add to current recursion path
            path.add(course)

            # Explore all prerequisites
            for p in pre[course]:
                if not dfs(p):
                    return False
            
            # Done exploring this course → remove from path
            path.remove(course)

            # Mark as fully processed (safe)
            visited.add(course)

            return True
        
        # Check every course (graph might be disconnected)
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True