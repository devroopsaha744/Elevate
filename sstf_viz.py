import turtle

def visualize_sstf_elevator(requests, start_position):
    screen = turtle.Screen()
    screen.title("SSTF Elevator Scheduling Visualization")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(1)

    # Draw floors (vertical representation)
    for floor in range(11):
        pen.penup()
        pen.goto(-50, floor * 50 - 250)
        pen.pendown()
        pen.write(f"Floor {floor}", align="right")

    # Draw start position
    pen.penup()
    pen.goto(0, start_position * 50 - 250)
    pen.pendown()
    pen.dot(20, "red")
    pen.write(f"Start: {start_position}", align="left")

    # SSTF logic
    current_position = start_position
    visited = set()
    while len(visited) < len(requests):
        # Find the closest request
        closest_request = None
        min_distance = float('inf')
        for request in requests:
            if request not in visited:
                distance = abs(request - current_position)
                if distance < min_distance:
                    min_distance = distance
                    closest_request = request
        # Move to the closest request
        pen.penup()
        pen.goto(0, current_position * 50 - 250)
        pen.pendown()
        pen.color("green")
        pen.goto(0, closest_request * 50 - 250)
        pen.dot(20, "blue")
        pen.write(f"Floor {closest_request}", align="left")
        current_position = closest_request
        visited.add(closest_request)

    turtle.done()

# Example usage
requests = [2, 7, 3, 9]
start_position = 5
visualize_sstf_elevator(requests, start_position)
