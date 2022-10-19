def Cipher_Zeroes(N):
    points = 0
    for item in N:
        if item == '0' or item == '6' or item == '9':
            points += 1
        if item == '8':
            points += 2
    points = points + 1 if points % 2 != 0 else points - 1 if points > 0 else 0
    return int(str(bin(points))[2:])


#if __name__ == '__main__':
    #a = input('n = ')
    #print(Cipher_Zeroes(a))


