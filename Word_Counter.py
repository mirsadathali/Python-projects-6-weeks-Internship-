def count_words(text):
    if not text.strip():
        return 0  # Return 0 for empty or whitespace-only input
    words = text.split()  # Split the text into words by whitespace
    return len(words)
def main():
    print("Welcome to the Word Counter!")
    print("Enter a sentence or paragraph below to count the number of words.")
    
    # Prompt the user for input
    user_input = input("Your input: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: No input detected. Please enter a valid sentence or paragraph.")
        return
    
    # Count the words and display the result
    word_count = count_words(user_input)
    print(f"\nThe number of words in your input is: {word_count}")


# Entry point of the script
if __name__ == "__main__":
    main()
