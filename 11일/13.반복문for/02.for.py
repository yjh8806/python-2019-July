#언패킹
a = [(1, 2), (3, 4), (5, 6)]
for i, j in a:
    print("%d + %d = %d"%(i, j, i + j))

filmFestival = {
"최우수 작품상":"택시운전사",
"감독상":"아이 캔 스피크",
"남우주연상":"송강호",
"여우주연상":"나문희"
}

for prize in filmFestival:
    print(prize)

for winner in filmFestival.values():
    print(winner)

#key와 value를 묶어서 들고옴
for prize_winner in filmFestival.items():
    print(prize_winner)

for prize, winner in filmFestival.items():
    print(prize + " : " + winner)
