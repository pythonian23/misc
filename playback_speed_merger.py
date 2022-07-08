def merge(*playbacks):
    START, END, SPEED = range(3)
    out = [playbacks[0]]
    for playback in playbacks[1:]:
        prev = out[-1]
        if prev[END] == playback[START] and prev[SPEED] == playback[SPEED]:
            prev[END] = playback[END]
        else:
            out.append(playback)
    return out


if __name__ == "__main__":
    p = [[0, 10, 0.5], [10, 30, 1], [30, 50, 1], [50, 70, 1], [70, 85, 2], [88, 95, 2]]
    print(merge(*p))
