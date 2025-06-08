main_menu = [
    "Меню",
    "добавить контакт",
    "удалить контакт",
    "изменить контакт",
    "поиск контакта",
    "Открыть файл",
    "Просмотр контактов",
    "Сохранить справочник",
    "Новый",
    "Выход",
]
contact_menu = [
    "Фамилия: ",
    "Имя: ",
    "Телефон: ",

]

menu_input_mess = f"Введите число от 1 до {len(main_menu)-1}:"
menu_input_error = "Некорректный ввод!"

file_open_sccessfully = "Файл был успешно открыт"
file_open_error = "Ошибка открытия файла {}"

file_save_sccessfully = "Файл был успешно сохранен"
file_save_error = "Ошибка сохранения файла {}"

add_contact_input = "Введите данные контакта:"
add_contact_error = "Контакт не был добавлен {}!"
add_contact_successfully = "Контакт {} был успешно добавлен в справочник!"

input_id_contact = "Введите ИД контакта для редактирования:"

edit_contact_error = "Контакт не был изменен {}!"
edit_contact_successfully = "Контакт {} был успешно изменен!"

del_contact_successfully = "Контакт {} был успешно удален"
del_contact_error = "Ошибка удаления контакта {}"
contacts_print_error = "Словарь пустой!"

input_find_data = "Введите строку для поиска:"
