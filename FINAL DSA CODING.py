#TASK A 
print("-"*20,"TASK A","-"*20)
print()
print('Implement stackto read and store locations for a route')
class RouteStack:
    def __init__(self):
        self.stack = []

    def push(self, locations):
        self.stack.extend(locations)

    def pop(self, num_locations):
        removed_locations = [self.stack.pop() for _ in range(num_locations) if self.stack]
        return removed_locations

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Route:", self.stack)


def main():
    vertices = ['DS', 'EH', 'FH', 'KP', 'MQ', 'HS', 'PS']
    adjacency_matrix = [
        [0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 0, 9, 3, 3],
        [0, 11, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0]
    ]

    stack = RouteStack()
    while True:
        print("\nMenu:")
        print("1. Append location ")
        print("2. Remove location ")
        print("3. Display current route ")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Available locations:", ", ".join(vertices))
            locations = [location.strip().upper() for location in input("Enter location(s) to append (comma-separated): ").split(',')]
            valid_locations = [location for location in locations if location in vertices]
            stack.push(valid_locations)
            print(f"Locations {' '.join(valid_locations)} appended to route.")

        elif choice == '2':
            num_locations = int(input("Enter the number of locations to remove: "))
            removed_locations = stack.pop(num_locations)
            if removed_locations:
                print(f"Locations {' '.join(removed_locations)} removed from route.")
            else:
                print("Route is empty.")

        elif choice == '3':
            stack.display()

        elif choice == '4':
            print("Bye...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


#adjacency matrix
print("-"*20,"TASK B","-"*20)
print()
print('(1) ADJACENCY MATRIX : ')
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    def add_edge(self, start, end, weight):
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        self.adj_matrix[start_idx][end_idx] = weight

    def display(self):
        print("      ", end="")
        for vertex in self.vertices:
            print(f"| {vertex} ", end="  ")
        print('|')
        print("  " + "-" * (8 * len(self.vertices)))

        for i, row in enumerate(self.adj_matrix):
            print(f"| {self.vertices[i]} ", end=" ")
            for weight in row:
                print(f"| {weight:<5}", end="")
            print("|")


# Example usage:
vertices = ['DS', 'EH', 'FH', 'KM', 'MQ', 'HS', 'PS']
adjacency_matrix = [
    [0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0],
    [15, 0, 0, 0, 9, 3, 3],
    [0, 11, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0]
]
graph = Graph(vertices)
for i in range(len(vertices)):
    for j in range(len(vertices)):
        if adjacency_matrix[i][j] != 0:
            graph.add_edge(vertices[i], vertices[j], adjacency_matrix[i][j])

graph.display()


graph = {
    'KP': [('DS', 15), ('MQ', 9), ('PS', 3), ('HS', 3)],
    'DS': [('EH', 7)],
    'FH': [('DS', 5)],
    'HS': [('FH', 4)], 
    'PS': [('MQ', 7)],
    'MQ': [('EH', 11)], 
}
print()

# Print the graph
print('(2) ADJACENCY LIST : ')
print()
print("From\tTo \tDistance(m)")
for vertex, neighbors in graph.items():
    for neighbor, weight in neighbors:
        print(f"{vertex} --> \t{neighbor} edge weight:\t{weight}")

print()

#TASKC
print("-"*20,"TASK C","-"*20)
print('Calculate the distance travelled for the activity.')
print()
class Graph:
    def __init__(self, vertices, adjacency_matrix):
        self.vertices = vertices
        self.adj_matrix = adjacency_matrix

    def get_distance(self, start, end):
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        return self.adj_matrix[start_idx][end_idx]


def main():
    vertices = ['DS', 'EH', 'FH', 'KP', 'MQ', 'HS', 'PS']
    adjacency_matrix = [
        [0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 0, 9, 3, 3],
        [0, 11, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0]
    ]

    graph = Graph(vertices, adjacency_matrix)

    total_distance = 0

    print('Checkpoint available : DS, EH, FH, KP, MQ, HS, PS')
    print('Please enter checkpoint one by one!')
    print()
    while True:
        start = input("Enter the starting checkpoint: ").strip().upper()
        end = input("Enter the ending checkpoint: ").strip().upper()

        if start not in vertices or end not in vertices:
            print("Invalid checkpoint! Please enter valid checkpoints.")
            continue

        distance = graph.get_distance(start, end)
        if distance == 0:
            print("No route found between the checkpoints.")
        else:
            total_distance += distance
            print(f"Distance traveled from {start} to {end}: {distance} m")
            print(f"Total distance traveled so far: {total_distance} m")

        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    print(f"Total distance traveled for the activity: {total_distance} m")


if __name__ == "__main__":
    main()

print()
#taskD
print("-"*20,"TASK D","-"*20)
print('Display the visited check points and the total distance travelled and marks earned on the output : ')
print('Please enter checkpoints one by one!')
print()
print('Checkpoint available : DS, EH, FH, KP, MQ, HS, PS')

class Graph:
    def __init__(self, vertices, adjacency_matrix):
        self.vertices = vertices
        self.adj_matrix = adjacency_matrix

    def get_distance(self, start, end):
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        return self.adj_matrix[start_idx][end_idx]


def calculate_marks(total_distance):
    if total_distance < 20:
        marks = 40
        bonus_marks = marks * 0.1
    else:
        marks = 20
        bonus_marks = 0
    return marks, bonus_marks


def display_checkpoints(visited_checkpoints):
    print("Visited checkpoints:")
    for start, end in visited_checkpoints:
        print(f"{start} -> {end}")


def main():
    vertices = ['DS', 'EH', 'FH', 'KP', 'MQ', 'HS', 'PS']
    adjacency_matrix = [
        [0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 0, 9, 3, 3],
        [0, 11, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0]
    ]

    graph = Graph(vertices, adjacency_matrix)

    total_distance = 0
    visited_checkpoints = []
    print()
    while True:
        start = input("Enter the starting checkpoint: ").strip().upper()
        end = input("Enter the ending checkpoint: ").strip().upper()

        if start not in vertices or end not in vertices:
            print("Invalid checkpoint! Please enter valid checkpoints.")
            continue

        distance = graph.get_distance(start, end)
        if distance == 0:
            print("No route found between the checkpoints.")
        else:
            total_distance += distance
            visited_checkpoints.append((start, end))
            print(f"Distance traveled from {start} to {end}: {distance} m")
            print(f"Total distance traveled so far: {total_distance} m")

        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    marks, bonus_marks = calculate_marks(total_distance)
    total_marks = marks + bonus_marks

    print("-"*40)
    display_checkpoints(visited_checkpoints)
    print("-"*40)
    print(f"Total distance traveled : {total_distance} m")
    print("-"*40)
    print(f"Marks earned : {marks}")
    print(f"Bonus marks : {bonus_marks:.2f}")
    print(f"Total marks earned: {total_marks:.2f}")
    print("-"*40)


if __name__ == "__main__":
    main()

print()
#TASK E
print("-"*20,"TASK E","-"*20)
print('Apply Dijsktra’s Algorithm to find the shortest path : ')
print()
print('Checkpoint available : DS, EH, FH, KP, MQ, HS, PS')
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    def add_edge(self, start, end, distance):
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        self.adj_matrix[start_idx][end_idx] = distance

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.vertices):
            min_vertex = min((distances[vertex], vertex) for vertex in self.vertices if vertex not in visited)[1]

            for idx, weight in enumerate(self.adj_matrix[self.vertices.index(min_vertex)]):
                if weight > 0:
                    if distances[min_vertex] + weight < distances[self.vertices[idx]]:
                        distances[self.vertices[idx]] = distances[min_vertex] + weight

            visited.add(min_vertex)

        return distances

def main():
    vertices = ['DS', 'EH', 'FH', 'KP', 'MQ', 'HS', 'PS']
    adjacency_matrix = [
        [0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 0, 9, 3, 3],  
        [0, 11, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0]
    ]

    graph = Graph(vertices)

    print()
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if adjacency_matrix[i][j] != 0:
                graph.add_edge(vertices[i], vertices[j], adjacency_matrix[i][j])

    start = input("Enter the starting checkpoint: ").strip().upper()
    end = input("Enter the ending checkpoint: ").strip().upper()

    distances = graph.dijkstra(start)
    total_distance = distances[end]

    print("\nDistances for each checkpoint:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}m")

    print(f"\nShortest path from {start} to {end}: {total_distance}m")
  
if __name__ == "__main__":
    main()
