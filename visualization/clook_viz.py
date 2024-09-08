from manim import *

class CLOOKElevator(Scene):
    def construct(self):
        # Define the floors and the requests
        requests = [1, 9, 4, 7, 3, 6]  # Requests
        initial_position = 5  # Starting floor
        total_floors = 10  # Total number of floors

        # Create a vertical array of floors
        floor_size = 0.5  # Size of the floor squares
        floor_gap = 0.1   # Gap between floors
        total_height = (total_floors + 1) * (floor_size + floor_gap)

        # Create the literal array of floors (blue squares)
        floors = VGroup()
        for i in range(total_floors + 1):
            floor = Square(side_length=floor_size, color=BLUE)
            floor.move_to(UP * (i * (floor_size + floor_gap) - total_height / 2))
            floor_label = Text(f"{i}", font_size=20).move_to(floor.get_center())
            floors.add(floor, floor_label)
        
        # Scale and center the floors group
        floors.scale(0.9)
        floors.move_to(ORIGIN)
        
        self.add(floors)
        
        # Create the elevator pointer
        pointer_base = Triangle(fill_color=YELLOW, fill_opacity=1, stroke_width=0).rotate(90 * DEGREES)
        pointer_base.scale(0.2)
        pointer_stick = Line(start=ORIGIN, end=RIGHT * 0.5, color=YELLOW)
        elevator_pointer = VGroup(pointer_base, pointer_stick)
        
        # Position the pointer to the right edge of the initial floor
        elevator_pointer.move_to(floors[initial_position * 2].get_right() + RIGHT * 0.1)
        
        self.add(elevator_pointer)
        
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
        
        # Display the algorithm name
        algorithm_text = Text("C-LOOK Algorithm", font_size=24).to_edge(DL)
        self.add(algorithm_text)
        
        # Function to animate the elevator pointer moving to a specific floor
        def move_elevator_to(floor_number, duration=0.5):
            target_position = floors[floor_number * 2].get_right() + RIGHT * 0.1  # Move to the right edge of the floor
            return elevator_pointer.animate.move_to(target_position)
        
        # Animate the elevator according to the C-LOOK algorithm
        self.wait(1)
        
        # Initialize calculations
        current_floor = initial_position
        total_distance = 0
        path = [initial_position]
        remaining_requests = set(requests)
        
        while remaining_requests:
            # Find the highest request
            highest_request = max(remaining_requests)
            
            # Move up to the highest request
            for floor in range(current_floor, highest_request + 1):
                if floor in remaining_requests:
                    # Move elevator to this floor
                    distance = floor - current_floor
                    total_distance += distance
                    path.append(floor)
                    
                    self.play(
                        distance_text.animate.become(Text(f"Distance: {total_distance}", font_size=24).to_edge(UR).shift(LEFT)),
                        path_text.animate.become(Text(f"Path: {path}", font_size=24).next_to(distance_text, DOWN))
                    )
                    self.play(move_elevator_to(floor))
                    self.play(request_numbers[requests.index(floor)].animate.set_color(PINK))
                    self.wait(0.5)
                    
                    remaining_requests.remove(floor)
                current_floor = floor
            
            # If there are still remaining requests, go back to the lowest request
            if remaining_requests:
                lowest_request = min(remaining_requests)
                
                # Only append the lowest request if it hasn't been added already
                if current_floor != lowest_request:
                    # Animate moving from current floor to the lowest request
                    self.play(
                        elevator_pointer.animate.move_to(floors[lowest_request * 2].get_right() + RIGHT * 0.1),
                        run_time=1
                    )
                    
                    # Update distance and path
                    total_distance += current_floor - lowest_request
                    path.append(lowest_request)
                    current_floor = lowest_request
                    
                    self.play(
                        distance_text.animate.become(Text(f"Distance: {total_distance}", font_size=24).to_edge(UR).shift(LEFT)),
                        path_text.animate.become(Text(f"Path: {path}", font_size=24).next_to(distance_text, DOWN))
                    )
                    self.wait(0.5)
        
        # Calculate average seek time
        avg_seek_time = total_distance / len(requests)
        
        # Display total distance and average seek time on the right side
        total_distance_text = Text(f"Total Distance: {total_distance}", font_size=24)
        avg_seek_time_text = Text(f"Avg Seek Time: {avg_seek_time:.2f}", font_size=24)
        
        stats_group = VGroup(total_distance_text, avg_seek_time_text).arrange(DOWN, aligned_edge=LEFT)
        stats_group.next_to(path_text, DOWN, buff=0.5).align_to(path_text, LEFT)
        
        self.play(Write(stats_group))
        self.wait(2)
