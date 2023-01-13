import heapq


def solution(jobs):
    answer = 0
    thq = []
    jobs.sort(key=lambda x: x[0])
    curr = 0

    for arr in jobs:
        heapq.heappush(thq, (arr[0], arr[1]))

    hq = []
    while len(thq) != 0:
        while len(thq) != 0 and thq[0][0] <= curr:
            start, d = heapq.heappop(thq)
            heapq.heappush(hq, (d, start))
        if len(hq) == 0:
            curr += 1
        if len(hq) != 0:
            duration, starttime = heapq.heappop(hq)
            answer += curr - starttime + duration
            curr = curr + duration

    while len(hq) != 0:
        duration, starttime = heapq.heappop(hq)
        answer += curr - starttime + duration
        curr = curr + duration

    return int(answer / len(jobs))