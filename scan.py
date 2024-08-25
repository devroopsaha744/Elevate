def scan(requests, start_position, disk_size):
    requests = sorted(requests)
    total_distance = 0
    current_position = start_position
    num_requests = len(requests)
    path = [start_position]
    
    # Determine the direction of movement
    if current_position < requests[0]:
        direction = 1  # Move right
    elif current_position > requests[-1]:
        direction = -1 # Move left
    else:
        direction = 1 if current_position < (disk_size // 2) else -1
    
    if direction == 1:
        # Move right
        for request in filter(lambda x: x >= current_position, requests):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
        # Move to end and then to start
        if current_position < disk_size - 1:
            total_distance += (disk_size - 1 - current_position) + (disk_size - 1 - requests[0])
            current_position = requests[0]
        # Move right again
        for request in filter(lambda x: x >= current_position, requests):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
            path.append(current_position)
    else:
        # Move left
        for request in filter(lambda x: x <= current_position, reversed(requests)):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
        # Move to start and then to end
        if current_position > 0:
            total_distance += current_position + (disk_size - 1 - requests[-1])
            current_position = requests[-1]
        # Move left again
        for request in filter(lambda x: x <= current_position, reversed(requests)):
            distance = abs(current_position - request)
            total_distance += distance
            current_position = request
            path.append(current_position)
    
    average_seek_time = total_distance / num_requests
    return total_distance, average_seek_time, path

# Example usage
requests = [4, 10, 15, 7]
start_position = 5
disk_size = 20
total_distance, average_seek_time, path = scan(requests, start_position, disk_size)
print("SCAN Total Distance:", total_distance)
print("SCAN Average Seek Time:", average_seek_time)
print("SCAN path:", path)