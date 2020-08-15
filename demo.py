n = int(input())
arr = list(map(int,input().split()))


def migratoryBirds(arr):
    freq_dict = Counter(arr)
    maxx=max(freq_dict.values())
    def get_key(val):
        for key,value in freq_dict.items():
            if val==value:
                return key

    return get_key(maxx)
migratoryBirds(arr)