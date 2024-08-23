def fcfs(requests, start_position):
    total_distance = 0
    total_response_time = 0
    current_position = start_position
    num_requests = len(requests)
    
    for i, request in enumerate(requests):
        distance = abs(current_position - request)
        total_distance += distance
        response_time = distance  # Assuming response time is proportional to distance
        total_response_time += response_time
        current_position = request
    
    average_seek_time = total_distance / num_requests
    average_response_time = total_response_time / num_requests
    
    return total_distance, average_seek_time, average_response_time

# Example usage
requests = [4, 10, 15, 7]
start_position = 5
total_distance, average_seek_time, average_response_time = fcfs(requests, start_position)
print("FCFS Total Distance:", total_distance)
print("FCFS Average Seek Time:", average_seek_time)
print("FCFS Average Response Time:", average_response_time)

print("Hello")