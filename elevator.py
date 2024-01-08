class Elevator:
    def __init__(self, total_floors):
        self.current_floor = 1
        self.total_floors = total_floors
        self.direction = "UP"
        self.requests = set()

    def request_floor(self, floor):
        if 1 <= floor <= self.total_floors:
            self.requests.add(floor)
            print(f"Request received for floor {floor}.")
        else:
            print("Invalid floor request.")

    def move(self):
        if not self.requests:
            print("No pending requests.")
            return

        next_floor = min(self.requests) if self.direction == "UP" else max(self.requests)
        self.requests.remove(next_floor)

        print(f"Moving {self.direction} to floor {next_floor}.")
        self.current_floor = next_floor

    def operate(self):
        while True:
            print(f"\nCurrent Floor: {self.current_floor}")
            self.move()
            self.direction = "UP" if self.direction == "DOWN" else "DOWN"
            user_input = input("Enter floor to request (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Exiting elevator program.")
                break

            try:
                requested_floor = int(user_input)
                self.request_floor(requested_floor)
            except ValueError:
                print("Invalid input. Please enter a floor number or 'q' to quit.")


def main():
    total_floors = 10  # Change this to the total number of floors in the building
    elevator = Elevator(total_floors)

    print("Welcome to the Elevator Simulator!")
    elevator.operate()


if __name__ == "__main__":
    main()
