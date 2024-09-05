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
    requests = [3, 15, 6, 18, 2, 10, 8, 12]
    initial_position = 5

    path, total_distance, avg_seek_time = SSTF(requests, initial_position)
    print("SSTF Path:", path)
    print("Total Distance:", total_distance)
    print("Average Seek Time:", avg_seek_time)

#Results
'''
SSTF Path: [5, 6, 8, 10, 12, 15, 18, 3, 2]
Total Distance: 29
Average Seek Time: 3.2222222222222223
'''
        
        