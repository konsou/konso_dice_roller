from parse import roll_string_from_input, markdown_roll_string_from_input

if __name__ == "__main__":
    print(roll_string_from_input("0d6"))
    print(roll_string_from_input("5d7+3"))
    print(roll_string_from_input("2d20-2"))

    print(markdown_roll_string_from_input("1d6"))
    print(markdown_roll_string_from_input("5d7+3"))
    print(markdown_roll_string_from_input("2d20-2"))

    # print(roll_string_from_input("4d2+4-4"))
