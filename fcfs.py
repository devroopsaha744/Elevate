def fcfs(requests, start_position):
    total_distance = 0
    total_response_time = 0
    current_position = start_position
    num_requests = len(requests)
    path = [start_position]
    
    for i, request in enumerate(requests):
        distance = abs(current_position - request)
        total_distance += distance
        current_position = request
        path.append(current_position)
    
    average_seek_time = total_distance / num_requests
    
    return total_distance, average_seek_time, path

# Example usage
requests = [4, 10, 15, 7]
start_position = 5
total_distance, average_seek_time, path = fcfs(requests, start_position)
print("FCFS Total Distance:", total_distance)
print("FCFS Average Seek Time:", average_seek_time)
print("FCFS Path taken by the Elevator:", path)

