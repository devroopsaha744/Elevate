def look(requests, start_position):
    requests = sorted(requests)
    total_distance = 0
    current_position = start_position
    num_requests = len(requests)
    path = [start_position]
    
    if current_position < requests[0]:
        # Move right first
        for request in filter(lambda x: x >= current_position, requests):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
        # Move back to the lowest request
        if requests:
            total_distance += abs(current_position - requests[0])
            current_position = requests[0]
        # Move right again
        for request in filter(lambda x: x > current_position, requests):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
    else:
        # Move left first
        for request in filter(lambda x: x <= current_position, reversed(requests)):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
        # Move back to the highest request
        if requests:
            total_distance += abs(current_position - requests[-1])
            current_position = requests[-1]
        # Move left again
        for request in filter(lambda x: x < current_position, reversed(requests)):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
            path.append(current_position)
    
    average_seek_time = total_distance / num_requests
    return total_distance, average_seek_time, path

# Example usage
requests = [4, 10, 1, 7]
start_position = 5
total_distance, average_seek_time, path = look(requests, start_position)
print("LOOK Total Distance:", total_distance)
print("LOOK Average Seek Time:", average_seek_time)
print("LOOK Path:", path)
