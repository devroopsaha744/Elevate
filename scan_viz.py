import turtle

def visualize_scan_elevator(requests, start_position, direction='up'):
    screen = turtle.Screen()
    screen.title("SCAN Elevator Scheduling Visualization")
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

    current_position = start_position
    requests.sort()

    # Determine direction and move accordingly
    if direction == 'up':
        for request in requests:
            if request >= current_position:
                pen.penup()
                pen.goto(0, current_position * 50 - 250)
                pen.pendown()
                pen.color("green")
                pen.goto(0, request * 50 - 250)
                pen.dot(20, "blue")
                pen.write(f"Floor {request}", align="left")
                current_position = request

        # After reaching the top, reverse direction
        for request in reversed(requests):
            if request < start_position:
                pen.penup()
                pen.goto(0, current_position * 50 - 250)
                pen.pendown()
                pen.color("green")
                pen.goto(0, request * 50 - 250)
                pen.dot(20, "blue")
                pen.write(f"Floor {request}", align="left")
                current_position = request
    else:
        for request in reversed(requests):
            if request <= current_position:
                pen.penup()
                pen.goto(0, current_position * 50 - 250)
                pen.pendown()
                pen.color("green")
                pen.goto(0, request * 50 - 250)
                pen.dot(20, "blue")
                pen.write(f"Floor {request}", align="left")
                current_position = request

        # After reaching the bottom, reverse direction
        for request in requests:
            if request > start_position:
                pen.penup()
                pen.goto(0, current_position * 50 - 250)
                pen.pendown()
                pen.color("green")
                pen.goto(0, request * 50 - 250)
                pen.dot(20, "blue")
                pen.write(f"Floor {request}", align="left")
                current_position = request

    turtle.done()

# Example usage
requests = [2, 7, 3, 9]
start_position = 5
visualize_scan_elevator(requests, start_position)
