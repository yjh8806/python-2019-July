vote = input("투표를 해주세요(A, B) : ").upper()
#aabbAAABB => A : 5, B : 4 => A가 이겼습니다~
voteA = vote.count('A')
voteB = vote.count('B')

print("A : %d, B : %d"%(voteA, voteB))
if voteA > voteB:
    print("A가 이겼습니다.")
elif voteA < voteB:
    print("B가 이겼습니다.")
else:
    print("비겼습니다.")
