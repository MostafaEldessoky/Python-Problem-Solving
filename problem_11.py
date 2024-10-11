

def birthdayCakeCandles(candles):
    count = 1
    candles.sort()
    for i in range(len(candles)-2,-1,-1):
        if candles[i] == candles[-1]:
            count += 1
        else:
            break
    print(count)
    

birthdayCakeCandles([3, 3, 3, 3])