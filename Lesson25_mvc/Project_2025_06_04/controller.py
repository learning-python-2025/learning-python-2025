import  view
import model

def start():
    while True:
        select = view.input_ouput()
        if select == 1:
            contact_data = view.input_ouput()
            result = model.add_contact(contact_data) 
            view.input_ouput(result)  
        elif select == 2:
            contact_id = view.input_ouput()
            result = model.delete_contact(contact_id) 
            view.input_ouput(result) 
        elif select == 3:
            contact_id = view.input_ouput()
            result = model.edit_contact(contact_id) 
            view.input_ouput(result) 
        elif select == 4:
            model.find_contact()
        elif select == 5:
            model.open_file()
        elif select == 6:
            model.view_contacts()
        elif select == 7:
            model.save_file()
        else:
            exit() 