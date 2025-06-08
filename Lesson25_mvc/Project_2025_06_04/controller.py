import view
import model
import text


def start():
    while True:
        view.show_menu()
        select = view.input_choice_user()

        def f_add():
            view.print_message(
                text.add_contact_input)
            list_contact_data = view.input_contact_data(text.contact_menu)
            contact_name = model.add_contact(
                list_contact_data)
            view.print_message(
                text.add_contact_successfully.format(contact_name))

        def f_del():
            list_contact_id = view.input_contact_data(
                [text.input_id_contact, ])

            result, massage = model.delete_contact(
                list_contact_id[0])
            if result:
                view.print_message(
                    text.del_contact_successfully.format(massage))
            else:
                view.print_message(
                    text.del_contact_error.format(massage))

        def f_edit():
            list_contact_id = view.input_contact_data(
                [text.input_id_contact, ])
            list_contact_data = view.input_contact_data(text.contact_menu)
            contact_name = model.edit_contact(
                list_contact_id[0], list_contact_data)
            view.print_message(
                text.edit_contact_successfully.format(contact_name))

        def f_find():
            list_contact_id = view.input_contact_data(
                [text.input_find_data, ])
            result = model.find_contact(list_contact_id[0])
            view.print_contacts(result)

        def f_open():
            result, message_error = model.open_file()
            if result:
                view.print_message(text.file_open_sccessfully)
            else:
                view.print_message(text.file_open_error.format(message_error))

        def f_print():
            if model.dict_data:
                view.print_contacts(model.dict_data)
            else:
                view.input_ouput(text.contacts_print_error)

        def f_save():
            result, message_error = model.save_file()
            if result:
                view.print_message(text.file_save_sccessfully)
            else:
                view.print_message(text.file_save_error.format(message_error))

        def f_exit():
            exit()
        menu_items_funcs = [
            f_add,
            f_del,
            f_edit,
            f_find,
            f_open,
            f_print,
            f_save,
            f_exit,
        ]

        menu_items_funcs[select-1]()
