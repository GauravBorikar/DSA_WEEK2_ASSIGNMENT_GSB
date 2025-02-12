#name:-Gaurav Borikar
# Checking if a string is a palindrome by ignoring non-alphabetical characters
def check_palindrome(input_string):
    cleaned_string = ""

    # Iterating through the string to clean it up
    for character in input_string:
        if character.isalpha():  # We only want to keep alphabetic characters
            cleaned_string += character.lower()  # Convert characters to lowercase

    # Checking if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


# Function to swap adjacent characters in a string
def swap_adjacent_characters(input_string):
    # Convert the string to a list so we can modify it
    char_list = list(input_string)

    # Loop through the list and swap adjacent elements
    for i in range(0, len(char_list) - 1, 2):
        char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

    # Convert the list back to a string
    return ''.join(char_list)


# Main program execution
def main():
    # Asking the user to input a string
    user_input = input("Please enter a string: ")

    # Checking if the entered string is a palindrome
    if check_palindrome(user_input):
        print("Yes, the string is a palindrome!")
    else:
        print("No, the string is not a palindrome!")

    # Calling the function to swap adjacent characters in the string
    swapped_string = swap_adjacent_characters(user_input)
    print("String after swapping adjacent characters:", swapped_string)


# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()

