import turtle

def visualize_fcfs_elevator(requests, start_position):
    screen = turtle.Screen()
    screen.title("FCFS Elevator Scheduling Visualization")
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

    # Move the elevator to each requested floor
    current_position = start_position
    for request in requests:
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
visualize_fcfs_elevator(requests, start_position)
