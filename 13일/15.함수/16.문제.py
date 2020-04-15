def my_avg(*args):
    return sum(args) / len(args)
def my_max(*args):
    MAX = 0
    for i in args:
        if MAX <= i:
            MAX = i
    return MAX

print("평균 : %.2f"%my_avg(97, 44, 31))
print("최대값 : %d"%my_max(99, 44, 31, 100))
