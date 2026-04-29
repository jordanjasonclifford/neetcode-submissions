class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list:
        # key = course
        # value = list of prerequisites for that course
        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        # This set tracks the current DFS path (recursion stack)
        # If we revisit a node in this set → cycle exists
        taken = set()

        def dfs(course):
            # If this course has no prerequisites left,
            # it's already been verified as "safe"
            if not pre[course]:
                return True
            
            # If we're visiting this course again in the SAME path,
            # we found a cycle → cannot finish
            if course in taken:
                return False
            
            # Add course to current path
            taken.add(course)

            # Try to complete all prerequisites
            for p in pre[course]:
                # If any prerequisite leads to a cycle → fail
                if not dfs(p):
                    return False
            
            # IMPORTANT OPTIMIZATION:
            # We've successfully checked this course and all its prereqs
            # → mark it as completed by clearing its prereq list
            # (memoization so we don’t recompute)
            pre[course] = []
            
            # Remove from current path (backtrack)
            taken.remove(course)

            return True
        
        # Try to DFS every course (handles disconnected graph)
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True