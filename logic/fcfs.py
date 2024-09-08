def calculate_metrics(path, start):
    total_distance = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))
    avg_seek_time = total_distance / len(path)
    return total_distance, avg_seek_time

def FCFS(requests, initial_position):
    path = [initial_position] + requests
    total_distance, avg_seek_time = calculate_metrics(path, initial_position)
    return path, total_distance, avg_seek_time

if __name__ == "__main__":
    requests = [1, 9, 4, 7, 3, 6]
    initial_position = 5

    path, total_distance, avg_seek_time = FCFS(requests, initial_position)
    print("FCFS Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

#Results
'''
FCFS Path: [5, 1, 9, 4, 7, 3, 6]
Total Distance: 27
Average Seek Time: 3.857142857142857
'''
