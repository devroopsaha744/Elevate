def sstf(requests, start_position):
    requests = sorted(requests)
    total_distance = 0
    current_position = start_position
    num_requests = len(requests)
    path = [start_position]
    
    while requests:
        closest_request = min(requests, key=lambda x: abs(current_position - x))
        distance = abs(current_position - closest_request)
        total_distance += distance
        current_position = closest_request
        path.append(current_position)

        requests.remove(closest_request)
    
    average_seek_time = total_distance / num_requests
    return total_distance, average_seek_time, path

# Example usage
requests = [4, 10, 15, 7]
start_position = 5
total_distance, average_seek_time, path = sstf(requests, start_position)
print("SSTF Total Distance:", total_distance)
print("SSTF Average Seek Time:", average_seek_time)
print("SSTF Path followed by the Elevator:", path)

        
        