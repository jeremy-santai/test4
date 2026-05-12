#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # Write your code here
    tracker = {}  # To track sign-in times
    users = []    # To store user IDs who meet the condition
    for i in logs:
        user_id, timestamp, action = i.split()
        timestamp = int(timestamp)
        if action == "sign-in":
            tracker[user_id] = timestamp  # Record the sign-in time
        elif action == "sign-out" and user_id in tracker:
            # Calculate time difference
            if timestamp - tracker[user_id] <= maxSpan:
                users.append(user_id)
    return sorted(users)
    #
    # WARNING: Please do not use GitHub Copilot, ChatGPT, or other AI assistants
    #          when solving this problem!
    #
    # We use these tools in our coding too, but in our interviews, we also don't
    # allow using these, and want to see how we do without them.
    #

if __name__ == '__main__':
    fptr = sys.stdout

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
