#귀찮은거 싫어해요 => 긴 코드를 줄이려고 노력...
def SUM(a, b):
    return a + b

SUM = lambda a, b:a + b
MUL = lambda a, b:a * b
print(SUM(10, 20))
print(MUL(10, 20))

funclist = [lambda a, b:a + b, lambda a, b:a * b]
print(funclist[0](10, 20))
print(funclist[1](10, 20))
