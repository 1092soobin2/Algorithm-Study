import math


def solution(n, stations, w):
    answer = 0

    no_signal = 1
    for station in stations:
        if (station - w) > no_signal:
            answer += math.ceil((station - w - no_signal) / (2 * w + 1))
        no_signal = station + w + 1

    if n + 1 > no_signal:
        answer += math.ceil((n + 1 - no_signal) / (2 * w + 1))

    return answer