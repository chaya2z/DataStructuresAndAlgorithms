def towers_of_Hanoi(n, frompeg, topeg, auxpeg):
    # First, move disk 1.
    if n == 1:
        print("Move disk 1 from peg", frompeg, "to peg", topeg)
        return

    # move n - 1 pegs from source to auxiliary.
    towers_of_Hanoi(n - 1, frompeg, auxpeg, topeg)

    print("Move disk", n, "from peg", frompeg, "to peg", topeg)

    # move n - 1 pegs from auxiliary to destination
    towers_of_Hanoi(n - 1, auxpeg, topeg, frompeg)


towers_of_Hanoi(3, "A", "B", "C")
