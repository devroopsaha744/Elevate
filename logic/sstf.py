def calculate_metrics(path, start):
    total_distance = sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))
    avg_seek_time = total_distance / len(path)
    return total_distance, avg_seek_time

def SSTF(requests, initial_position):
    path = [initial_position]
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - path[-1]))
        path.append(closest_request)
        requests.remove(closest_request)
    total_distance, avg_seek_time = calculate_metrics(path, initial_position)
    return path, total_distance, avg_seek_time

if __name__ == "__main__":
    requests = [1, 9, 4, 7, 3, 6]
    initial_position = 5

    path, total_distance, avg_seek_time = SSTF(requests, initial_position)
    print("SSTF Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

#Results
'''
SSTF Path: [5, 4, 3, 1, 6, 7, 9]
Total Distance: 12
Average Seek Time: 1.7142857142857142
'''
        
        