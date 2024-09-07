def calculate_metrics(path, start):
    total_distance = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))
    avg_seek_time = total_distance / len(path)
    return total_distance, avg_seek_time

def FCFS(requests, initial_position):
    path = [initial_position] + requests
    total_distance, avg_seek_time = calculate_metrics(path, initial_position)
    return path, total_distance, avg_seek_time

if __name__ == "__main__":
    requests = [3, 15, 6, 18, 2, 10, 8, 12]
    initial_position = 5

    path, total_distance, avg_seek_time = FCFS(requests, initial_position)
    print("FCFS Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

#Results
'''
FCFS Path: [5, 3, 15, 6, 18, 2, 10, 8, 12]
Total Distance: 65
Average Seek Time: 7.222222222222222
'''