from parser import parse_input, roll_string_from_input

if __name__ == "__main__":
    print(parse_input("5d6+5"))
    print(parse_input("2d20-2"))
    print(roll_string_from_input("1d6"))
    print(roll_string_from_input("5d7+3"))
    print(roll_string_from_input("2d20-2"))
