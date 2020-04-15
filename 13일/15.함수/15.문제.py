def login(ac, id, pw): #ac = account
    if id in ac:
        if pw == ac[id]:
            print("%s님이 로그인했습니다."%id)
        else:
            print("비밀번호가 다릅니다.")
    else:
        print("등록되지 않은 아이디입니다.")

account = {"pomin615":"0123", "thdehdduf20":"4567"}
uid = input("ID : ")
upw = input("PW : ")
login(account,uid,upw)
