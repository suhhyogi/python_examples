def countdown(times):
    print(times)
    if times == 0:
        return times
    else:
        countdown(times - 1)

countdown(10)