class SeatNum:
    """
    Small Wrapper-Class for Airplane SeatNumbers
    """
    def __init__(self, pos=str(), seat=dict()):
        if pos is not None:
            seat = SeatNum.parse_pos(pos)

        self.row = seat.get('row')
        self.seat = seat.get('seat')

    def __str__(self):
        return f"{self.row}{self.seat}"

    def __lt__(self, other):
        """
        Comparing 2 seatnumbers, seats are ordered by row and within
        a row by seats at the Windows {'A', 'D'}
        and seats at the aisle {'B', 'C'},

        Numbers should be comaprable by row and within the same row by an aisle
        or window-position.
        """
        if self.row != other.row:
            return self.row < other.row
        else:
            if self.seat in {'B', 'C'} and other.seat in {'A', 'D'}:
                return True
            return False

    @classmethod
    def parse_pos(cls, pos):
        row = list()
        seat = list()
        for c in pos:
            if c.isdigit():#alpha():
                row.append(c)
            elif c.isalpha():
                seat.append(c)
        row = int(''.join(row))
        seat = ''.join(seat)
        return {'row':row, 'seat':seat}


def get_boarding_groups(ll, stride=4):
    res = list()
    for i, val in enumerate(ll[::stride]):
        res.append(f"{'*'*(i+1)}BG{i+1} - {', '.join([x.__str__() for x in ll[i*stride:i*stride+stride]])}")
    return res


if __name__ == '__main__':
    ll = [
        SeatNum('11A'),
        SeatNum('3A'),
        SeatNum('11C'),
        SeatNum('3B'),
        SeatNum('16A'),
        SeatNum('11B'),
        SeatNum('3D'),
        SeatNum('11D'),
        SeatNum('3C')

    ]

    ll.sort(reverse=False)

    print(*ll)
    print(*get_boarding_groups(ll))
