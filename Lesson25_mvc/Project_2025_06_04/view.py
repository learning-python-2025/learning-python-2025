import text


def show_menu():
    for idx, item in enumerate(text.main_menu):
        if idx:
            print(f'\t{idx}. {item}')
        else:
            print(item)


def input_choice_user():
    while True:
        selection = int(input(text.menu_input_mess))
        if selection in range(1, len(text.main_menu)):
            return selection
        else:
            print(text.menu_input_error)


def input_contact_data(messages: list[str]):
    result = []
    for entry in messages:
        result.append(input(entry))
    return result


def print_message(message: str):
    print("-------------------------------")
    print(f"\t {message}")
    print("-------------------------------")


def input_ouput(result):
    if result:
        print(text.edit_contact_successfully)
    else:
        print(text.edit_contact_error)


def input_user_data(messages: list[str]):
    pass


def print_contacts(dict: dict[str, dict]):
    print("\nСписок контактов:\n")
    print("-------------------------------")
    for id_contact, contact in dict.items():
        print(f"ИД контакта: {id_contact}")
        for key, value in contact.items():
            print(f"\t{key} : {value}")
        print("-------------------------------")
