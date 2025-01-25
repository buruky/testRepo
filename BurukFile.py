def print_multiplication_table():
    # Print the header row
    print("   |", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print("\n" + "-" * 45)

    # Print each row of the table
    for row in range(1, 11):
        print(f"{row:2} |", end="")
        for col in range(1, 11):
            print(f"{row * col:4}", end="")
        print()

if __name__ == "__main__":
    print("Multiplication Table (1 to 10):")
    print_multiplication_table()