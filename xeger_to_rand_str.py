from xeger import Xeger
_x = Xeger()
for _ in range(20):
   testStr = _x.xeger(r'([a-z])(\d{1,2}|[AJQK])')
   print(testStr)