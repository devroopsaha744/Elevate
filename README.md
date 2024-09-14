# Elevate

This project implements and visualizes various disk scheduling algorithms using the analogy of elevators in a building. The primary algorithms include FCFS, SSTF, SCAN, LOOK, and their circular versions. By treating each request as a floor in a building, we demonstrate how these scheduling algorithms optimize the movement of the elevator (or disk head) to minimize the total distance traveled and improve efficiency.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [FCFS (First-Come, First-Served)](#fcfs-first-come-first-served)
  - [SSTF (Shortest Seek Time First)](#sstf-shortest-seek-time-first)
  - [SCAN](#scan)
  - [LOOK](#look)
  - [C-SCAN](#c-scan)
  - [C-LOOK](#c-look)
- [Metrics](#metrics)
  - [Total Distance Traveled](#total-distance-traveled)
  - [Average Seek Time](#average-seek-time)
- [Installation](#installation)
- [Usage](#usage)
- [Visualization](#visualization)
- [Read More](#read-more)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Elevator algorithms help us understand how disk scheduling works in operating systems. This project simplifies these concepts by using a relatable analogy: elevators in a building. The project simulates how different scheduling algorithms like FCFS, SSTF, SCAN, LOOK, and their circular counterparts behave in an elevator system when servicing requests for different floors.

## Algorithms

### FCFS (First-Come, First-Served)
The elevator handles requests in the exact order they arrive, leading to potential inefficiencies if requests are far apart.

### SSTF (Shortest Seek Time First)
The elevator moves to the nearest floor requested from its current position, optimizing for minimal travel distance between stops.

### SCAN
The elevator moves in one direction, servicing requests, and then reverses direction once it hits the end of its range, ensuring that all requests are handled.

### LOOK
An optimized version of SCAN, where the elevator moves in one direction but only goes as far as the furthest request, avoiding unnecessary movement to the building's limits.

### C-SCAN
Similar to SCAN, but after reaching the highest requested floor, the elevator jumps back to the start (lowest floor) and continues in the same direction.

### C-LOOK
An optimized circular version of LOOK, where the elevator moves in one direction, services all requests, and jumps back to the first requested floor without traveling to extremes.

## Metrics

### Total Distance Traveled
The total number of floors traveled by the elevator while servicing all requests.

### Average Seek Time
The average number of floors between requests, provides an efficiency metric for each algorithm.


## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/elevator-scheduling-visualization.git
    cd elevator-scheduling-visualization
    ```

2. **Analyze the Algorithms**:
   - Navigate to the `analysis` folder to explore detailed analysis of the algorithms.
   - Open `analysis/analysis.ipynb` using Jupyter Notebook to examine the code and visualizations of various metrics like total distance traveled and average seek time.
   
3. **View Plots**:
   - Inside the `analysis/plots` folder, you'll find visual representations of how each algorithm performs, helping you understand their efficiency in terms of distance and time.

4. **Explore Algorithm Logic**:
   - The `logic` folder contains the code for each scheduling algorithm. This is where you can dive into how FCFS, SSTF, SCAN, LOOK, and their variations are implemented.

5. **Watch Simulations**:
   - In the `animations` folder, you'll find simulation videos demonstrating how the elevator moves according to each algorithm, offering a visual representation of the algorithms in action.

6. **Manim Visualizations**:
   - The `visualization` folder contains the Manim code used to generate the elevator scheduling animations. You can run the Manim scripts to create custom visualizations or tweak them according to your needs.

---



## Read More

For a deeper understanding of these algorithms and their real-world implications, check out my Medium article:

[Exploring Elevator Scheduling Algorithms in Operating Systems](https://medium.com/your-article-link)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you'd like to improve the project or add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

