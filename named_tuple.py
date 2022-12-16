from collections import namedtuple
Score = namedtuple('Score', ['Chinese', 'English', 'math'])
s1 = Score(9, 6, 11)
print(s1)
print(s1.Chinese)
