


def staircase(n):
    output: str = ""
    for _ in range(n):
        output += " "
    for i in range(1,n+1):
        output = output[:n-i]
        output += "#"*i
        print(output)

staircase(6)