def input_error(func): #processing of input error
    def wrapper(contacts, *args):
        try:
            result = func(contacts, *args)
        except IndexError:
            result = 'Enter a name(surname) and phone number!'
        except KeyError:
            result = 'Enter a phone number!'
        except ValueError:
            result = 'Phone number is incorrect!'
        return result

    return wrapper


def greet(*args):
    return "How can I help you?"


@input_error
def add(contacts, *args): # add info to system(list of users)
    name, surname, m_phone = args[0], args[1], args[2]
    full_name = name + ' ' + surname
    contacts[full_name] = m_phone
    return f"New user {full_name}, phone - {contacts[full_name]}"


@input_error
def change(contacts, *args): # change data in system(list of users)
    name, surname, m_phone = args[0], args[1], args[2]
    full_name = name + ' ' + surname
    prev_num = contacts[full_name]
    contacts[full_name] = m_phone
    return f"{full_name} number changed from {prev_num} to {m_phone}"


@input_error
def phone(contacts, *args): # update phone in system(list of users)
    name, surname = args[0], args[1]
    full_name = name + ' ' + surname
    return contacts[full_name]


def show_all(contacts, *args):
    return contacts


def goodbye(*args):
    print("Good bye!")
    return None
