def construct_lps_array(string) -> list[int]:
    lps = []
    lps.append(0)
    l = len(string)
    for i in range(1, l):
        x = lps[i-1]
        while (string[i] != string[x]):
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps.append(x+1)
    return lps


string = "adecvsadrpvadcs"
print(string)
print(construct_lps_array(string))
