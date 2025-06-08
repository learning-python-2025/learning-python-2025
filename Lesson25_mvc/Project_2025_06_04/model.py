import json

dict_path = 'Telefon_directory.json'
dict_data = {}
DICT_KEYS = [
    "first_name",
    "name",
    "phone",
]


def add_contact(contact_data: list[str]) -> str:

    new_contact = {}
    for idx, key in enumerate(DICT_KEYS):
        new_contact[key] = contact_data[idx]
    index = int(max(dict_data)) if dict_data else 0
    dict_data[index+1] = new_contact
    return new_contact[DICT_KEYS[0]]


def delete_contact(contact_id: str) -> tuple[bool, str]:
    try:
        del_contact = dict_data.pop(contact_id)
        return True, del_contact[DICT_KEYS[0]]
    except Exception as e:
        return False, e


def edit_contact(contact_id: str, contact_data: list[str]) -> str:

    edit_contact = dict_data[contact_id].copy()
    for idx, key in enumerate(DICT_KEYS):
        if contact_data[idx]:
            edit_contact[key] = contact_data[idx]
    dict_data[contact_id] = edit_contact
    return edit_contact[DICT_KEYS[1]]


def find_contact(find_str: str) -> str:
    result = {}
    for key, contact in dict_data.items():
        if find_str.lower() in ' '.join(contact.values()).lower():
            result[key] = contact
    return result


def open_file() -> tuple:
    global dict_data
    try:
        with open(dict_path, 'r', encoding='utf-8') as file:
            dict_data = json.load(file)
        return True, ""
    except Exception as e:
        return False, e


def save_file() -> tuple:
    try:
        with open(dict_path, 'w', encoding='utf-8') as file:
            json.dump(dict_data, file, indent=4, ensure_ascii=False)
        return True, ""
    except Exception as e:
        return False, e
