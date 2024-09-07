import streamlit as st
from PIL import Image, ImageDraw
import time

# Function to simulate FCFS (First-Come-First-Serve) algorithm
def fcfs(requests, head):
    path = [head] + requests
    return path

# Function to draw the building and elevator
def draw_elevator(floor, max_floor=10, width=100, height=500):
    # Create a blank image for the building
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Calculate the height of each floor
    floor_height = height / max_floor

    # Draw the floors
    for f in range(max_floor):
        y_top = int(f * floor_height)
        y_bottom = int((f + 1) * floor_height)
        draw.rectangle([0, y_top, width, y_bottom], outline="black", fill="#E0E0E0")

    # Draw the elevator as a rectangle on the current floor
    elevator_y_top = int((max_floor - floor - 1) * floor_height)
    elevator_y_bottom = int((max_floor - floor) * floor_height)
    draw.rectangle([10, elevator_y_top, width - 10, elevator_y_bottom], fill="orange")

    # Convert the image to streamlit format and display
    st.image(img, caption=f"Elevator at Floor {floor}", use_column_width=False)

# Streamlit app
st.title("Elevator Scheduling Algorithms Simulation")

# User input for the elevator requests
head = st.slider("Initial Head Position (Floor)", 0, 10, 5)
requests = st.multiselect("Request Floors", list(range(0, 11)), [2, 7, 9])

if st.button("Simulate FCFS"):
    # FCFS Algorithm
    path = fcfs(requests, head)

    # Visualize Elevator Movement
    st.subheader("Elevator Movement Visualization")
    
    for floor in path:
        draw_elevator(floor, max_floor=10, width=100, height=500)
        time.sleep(1)  # Pause for animation effect
