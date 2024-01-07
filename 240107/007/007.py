class Spy:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time


s_code, m_point, time = tuple(input().split())
s = Spy(s_code, m_point, time)

print("secret code :", s.code)
print("meeting point :", s.point)
print("time :", s.time)