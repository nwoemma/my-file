def test_range(n):
    if n in range(
        int(input("enter a number: ")),
        int(input("enter another number: "))
    ):
        print("%s is in range" %str(n))
    else:
        print("the number is outside the range. ")
test_range(int(input("test a number: ")))