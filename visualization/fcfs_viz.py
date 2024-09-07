from manim import *

class FCFSElevator(Scene):
    def construct(self):
        # Define the floors and the requests
        requests = [3, 7, 2, 9]
        initial_position = 5  # Starting floor
        
        # Create a vertical array of floors
        total_floors = 10
        floor_size = 0.8
        floor_gap = 0.2
        total_height = total_floors * (floor_size + floor_gap)
        
        # Create the literal array of floors (blue squares)
        floors = VGroup()
        for i in range(total_floors):
            floor = Square(side_length=floor_size, color=BLUE)
            floor.move_to(UP * (i * (floor_size + floor_gap) - total_height / 2))
            floor_label = Text(f"{i}", font_size=24).move_to(floor.get_center())
            floors.add(floor, floor_label)
        
        self.add(floors)
        
        # Create the elevator (yellow square) at the initial position
        elevator = Square(side_length=floor_size, color=YELLOW)
        elevator.move_to(UP * (initial_position * (floor_size + floor_gap) - total_height / 2))
        self.add(elevator)
        
        # Create text boxes for distance and path
        distance_text = Text("Distance: 0", font_size=24).to_edge(UR).shift(LEFT)
        path_text = Text(f"Path: [{initial_position}]", font_size=24).next_to(distance_text, DOWN)
        self.add(distance_text, path_text)
        
        # Display requests list with individual Text objects
        requests_text = Text("Requests: ", font_size=24).to_edge(UL)
        request_numbers = VGroup()
        for i, request in enumerate(requests):
            number = Text(str(request), font_size=24)
            if i > 0:
                number.next_to(request_numbers[-1], RIGHT, buff=0.2)
            else:
                number.next_to(requests_text, RIGHT)
            request_numbers.add(number)
        self.add(requests_text, request_numbers)
        
        # Function to animate the elevator moving to a specific floor
        def move_elevator_to(floor_number, duration=2):
            target_y = UP * (floor_number * (floor_size + floor_gap) - total_height / 2)
            return elevator.animate.move_to(target_y)
        
        # Animate the elevator according to the FCFS algorithm
        self.wait(1)
        
        # Initialize calculations
        previous_floor = initial_position
        total_distance = 0
        path = [initial_position]
        
        for i, floor in enumerate(requests):
            # Calculate distance
            distance = abs(floor - previous_floor)
            total_distance += distance
            
            # Update path
            path.append(floor)
            
            # Update distance and path text
            self.play(
                distance_text.animate.become(Text(f"Distance: {total_distance}", font_size=24).to_edge(UR).shift(LEFT)),
                path_text.animate.become(Text(f"Path: {path}", font_size=24).next_to(distance_text, DOWN))
            )
            
            # Move elevator and highlight the request
            self.play(
                move_elevator_to(floor),
                request_numbers[i].animate.set_color(PINK)
            )
            
            self.wait(1)
            
            previous_floor = floor
        
        # Calculate average seek time
        avg_seek_time = total_distance / len(requests)
        
        # Display total distance and average seek time on the right side
        total_distance_text = Text(f"Total Distance: {total_distance}", font_size=24)
        avg_seek_time_text = Text(f"Avg Seek Time: {avg_seek_time:.2f}", font_size=24)
        
        stats_group = VGroup(total_distance_text, avg_seek_time_text).arrange(DOWN, aligned_edge=LEFT)
        stats_group.next_to(path_text, DOWN, buff=0.5).align_to(path_text, LEFT)
        
        self.play(Write(stats_group))
        self.wait(3)