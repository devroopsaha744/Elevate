def calculate_metrics(path, start):
    total_distance = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))
    avg_seek_time = total_distance / len(path)
    return total_distance, avg_seek_time

def CLOOK(requests, start, end, initial_position):
    requests = sorted(requests)
    path = []
    
    if initial_position <= start:
        # Move upwards to handle all requests
        path = [initial_position] + requests
    elif initial_position >= end:
        # Handle all requests from the top
        path = [initial_position] + requests
    else:
        # Split requests into those above and below the initial position
        above = [r for r in requests if r >= initial_position]
        below = [r for r in requests if r < initial_position]
        # Move upwards, then jump to the lowest request and continue upwards
        path = [initial_position] + above + below
    
    total_distance, avg_seek_time = calculate_metrics(path, initial_position)
    return path, total_distance, avg_seek_time



if __name__ == "__main__":
    requests = [1, 9, 4, 7, 3, 6]
    initial_position = 5
    start = 0
    end = 10

    path, total_distance, avg_seek_time = CLOOK(requests, start, end, initial_position)
    print("CLOOK Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

    #Results
'''
CLOOK Path: [5, 6, 7, 9, 1, 3, 4]
Total Distance: 15
Average Seek Time: 2.142857142857143
'''

    
