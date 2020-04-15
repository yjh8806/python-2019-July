def change_name(a,b):
    return b + " " + a
firstname = input("성을 입력 : ")
lastname = input("이름을 입력 : ")
print(change_name(firstname,lastname))

def change_name(a):
    x,y = a.split() #공백을 기준으로 나눠서 위치를 바꿔줌
    return y + " " + x
name = input("이름 입력 : ")
print(change_name(name))
