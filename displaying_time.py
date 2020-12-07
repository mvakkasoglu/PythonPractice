# Write a program that obtains hours, minutes
# and remaining seconds from seconds.

# example case:
# input: 130sec
# output: 2min and 10secs

n = int(input("enter seconds: "))


def convert(seconds):
    hour = seconds // 3600  # 1 hr = 3600 seconds --> floor division finds how many hours
    seconds = seconds % 3600  # remainder is minutes + seconds
    minutes = seconds // 60  # 1 min = 60 seconds --> floor division finds how many mins
    seconds %= 60  # remainder is the seconds

    # return "%d:%02d:%02d" % (hour, minutes, seconds)  # (h:mm:ss)
    return "{} hours, {} minutes, {} seconds".format(hour, minutes, seconds)


# Driver program

print(convert(n))
