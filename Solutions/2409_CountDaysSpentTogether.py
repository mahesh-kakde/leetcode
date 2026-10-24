arriveAlice1, leaveAlice1, arriveBob1, leaveBob1 = "08-15", "08-18", "08-16", "08-19"
arriveAlice2, leaveAlice2, arriveBob2, leaveBob2 = "10-01", "10-31", "11-01", "12-31"

def sol(arriveAlice, leaveAlice, arriveBob, leaveBob):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def convert(date):
        month, day = map(int, date.split('-'))
        return sum(days[:month - 1]) + day

    start = max(convert(arriveAlice), convert(arriveBob))
    end = min(convert(leaveAlice), convert(leaveBob))

    return max(0, end - start + 1)

print(sol(arriveAlice1, leaveAlice1, arriveBob1, leaveBob1))
print(sol(arriveAlice2, leaveAlice2, arriveBob2, leaveBob2))