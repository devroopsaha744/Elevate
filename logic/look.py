def calculate_metrics(path, start):
    total_distance = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))
    avg_seek_time = total_distance / len(path)
    return total_distance, avg_seek_time

def LOOK(requests, start, end, initial_position):
    requests = sorted(requests)
    path = []
    if initial_position <= start:
        path = [start] + requests
    elif initial_position >= end:
        path = requests + [end]
    else:
        path = [r for r in requests if r >= initial_position] + [r for r in reversed(requests) if r < initial_position]
    path = [initial_position] + path
    total_distance, avg_seek_time = calculate_metrics(path, initial_position)
    return path, total_distance, avg_seek_time

if __name__ == "__main__":
    requests = [1, 9, 4, 7, 3, 6]
    initial_position = 5
    start = 0
    end = 10

    path, total_distance, avg_seek_time = LOOK(requests, start, end, initial_position)
    print("LOOK Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

#Results
'''
LOOK Path: [5, 6, 7, 9, 4, 3, 1]
Total Distance: 12
Average Seek Time: 1.7142857142857142

'''