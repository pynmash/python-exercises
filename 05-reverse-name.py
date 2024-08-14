def reverse_name(first_name, last_name):
    return f"{last_name} {first_name}"


def backwards_name(first_name, last_name):
    name = first_name + " " + last_name
    backwards_name_str = name[::-1]
    return backwards_name_str


def get_name():
    first_name = input("Please enter your first name: ").strip()
    last_name = input("Please enter your last name: ").strip()
    return (first_name, last_name)


name = get_name()
print(reverse_name(*name))
print(backwards_name(*name))
