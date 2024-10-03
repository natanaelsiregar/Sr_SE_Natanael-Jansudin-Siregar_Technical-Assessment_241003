class ArithmeticSequence:
    def __init__(self, first_term=2, difference=3):
        """
        Initialize the arithmetic sequence with the first term and common difference.

        Parameters:
        first_term (int): The first term of the sequence (default is 2).
        difference (int): The common difference between terms (default is 3).
        """
        self.first_term = first_term
        self.difference = difference

    def generate_sequence(self, n):
        """
        Generate the arithmetic sequence with 'n' terms.

        Parameters:
        n (int): Number of terms in the sequence.

        Returns:
        list: A list containing the arithmetic sequence.
        """
        sequence = []  # Initialize list to store the sequence
        for i in range(n):
            term = self.first_term + i * self.difference  # Calculate the i-th term
            sequence.append(term)  # Add the term to the list
        return sequence

    def sequence_to_string(self, n):
        """
        Generate the arithmetic sequence and return it as a string without spaces.

        Parameters:
        n (int): Number of terms in the sequence.

        Returns:
        str: A string containing the arithmetic sequence without spaces.
        """
        sequence = self.generate_sequence(n)  # Generate the sequence
        return ','.join(map(str, sequence))  # Convert list to string without spaces


def main():
    try:
        # Get the number of terms from user input
        n = int(input("Input: "))  # Mengambil input dari pengguna
        
        # Ensure the input is a positive integer
        if n <= 0:
            print("Please enter a positive integer for the number of terms.")
            return

        # Create an instance of ArithmeticSequence
        seq = ArithmeticSequence()  # Using default first term and difference
        # Generate and display the arithmetic sequence
        output_str = seq.sequence_to_string(n)  # Get sequence as string
        print(f"Output: {output_str}")  # Display result

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()