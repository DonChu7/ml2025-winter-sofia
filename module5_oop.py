class NumberProcessor:
    def __init__(self):
        self.N = None
        self.numbers = []
        self.X = None

    def get_inputs(self):
        while True:
            N_input = input("Enter a positive integer N (or type 'exit' to quit): ")
            if N_input.lower() == 'exit':
                print("Exiting the program...")
                return False
            try:
                self.N = int(N_input)
                if self.N <= 0:
                    print("N must be a positive integer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer or type 'exit' to quit.")
        
        for i in range(self.N):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        
        while True:
            try:
                self.X = int(input("Enter an integer X to search for: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        return True

    def search_x(self):
        if self.X in self.numbers:
            return self.numbers.index(self.X) + 1  # 1-based index
        return -1

    def run(self):
        if self.get_inputs():
            result = self.search_x()
            print(f"\nSearch result: {result}")
            print("\n" + "=" * 30 + "\n")

if __name__ == "__main__":
    processor = NumberProcessor()
    processor.run()