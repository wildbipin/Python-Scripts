# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores.
# Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains . The second line contains an array of integers each separated by a space.

# Output Format
# Print the runner-up score.

def runner_up(arr):
    arr_sorted = list(set(arr))
    arr_sorted.sort(reverse=True)
    return arr_sorted[1]
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_place = runner_up(arr)
    print(second_place)