class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        len_students = len(students)
        student_queue = deque(students)
        sandwich_stack = []
        for sandwich in reversed(sandwiches):
            sandwich_stack.append(sandwich)
        served = 0
        while student_queue and served < len(student_queue):
            if sandwich_stack[-1] == student_queue[0]:
                sandwich_stack.pop()
                student_queue.popleft()
                served = 0
            else:
                student_queue.append(student_queue[0])
                student_queue.popleft()
                served += 1
        return len(student_queue)