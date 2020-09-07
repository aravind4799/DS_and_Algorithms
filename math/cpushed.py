# arrival:7  2
# ending: 12 7

# return total time taken to end= 26

arrival = list(map(int,input().rstrip().split()))
burst = list(map(int,input().rstrip().split()))

d={}

for i,j in zip(arrival,burst):
    d[i]=j

sorted_arrival=sorted(d.keys())

total=0
total=sorted_arrival[0]+d[sorted_arrival[0]]

for time in sorted_arrival[1:]:
    if time<=total:
        total+=d[time]
    else:
        waiting_time = time - total
        total+=waiting_time
        total+=d[time]
print(total)


