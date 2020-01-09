from login_info import check_password


def add_account():
    print('Thanks for your interest to create an account.')
    ac = input("Enter Account Number: ")
    name = input("Enter Your Name: ")
    email = input("Enter Your E-mail: ")
    # number = input("Enter Your Phone Number: ")
    number = str(phone_number())
    password = check_password()
    deposit_amount = str(amount())
    with open("atm_software_db.txt", "a", newline='') as a:
        a.write('\n' + ac + "," + name + "," + email + "," + number + "," + password + "," + deposit_amount)
    print('Account created successfully')


def phone_number ():
    try:
        number = int(input("Enter Your Phone Number: "))
        return number
    except Exception as e:
        return phone_number()


def amount():
    try:
        amount_ = int(input("Deposit amount (Taka): "))
        return amount_
    except Exception as e:
        return amount()

def information_update(uid, passw):
    with open('atm_software_db.txt', 'r') as read_info:
        data = read_info.read()
        # new_line_data = data.split('\n')
        with open('atm_software_db.txt', 'w') as write_info:
            for datas in data.split('\n'):
                if datas:
                    ac, name, email, mobile_number, password, balance = datas.split(',')
                    if uid == ac and passw == password:
                        ex_balance = balance
                        balance = substraction(ex_balance)
                    write_info.write(ac + "," + name + "," + email + "," + mobile_number + "," + password + "," + balance + '\n')


def substraction(existing):
    new = input('Enter amount to cash out: ')
    if int(existing) > int(new):
        if int(new) % 500 == 0:
            balance = str(int(existing) - int(new))
            return balance
        else:
            print("✘ Amount must be multiple of 500.\nWe don't have smaller bank-notes, thank you.\n\n")
            return existing
    else:
        print('You have no enough money to cash out.')
        return existing


def all_information_check(uid, passw, view_flag='0'):
    with open('atm_software_db.txt', 'r') as read_balance:
        data = read_balance.read()
        # new_line_data = data.split('\n')
        for datas in data.split('\n'):
            ac, name, email, mobile_number, password, balance = datas.split(',')
            if uid == ac and passw == password:
                if view_flag == '1':
                    print('Current balance: {}'.format(balance))
                    break
                elif view_flag == '2':
                    return balance
                elif view_flag == '3':
                    print('Account Number: {}'.format(ac))
                    print('Full Name: {}'.format(name))
                    print('Email Address: {}'.format(email))
                    print('Mobile Number: {}'.format(mobile_number))
                    print('Current balance: {}'.format(balance))
                elif view_flag == "4":
                    return password
                break



def user_pass_check(uid, passw):
    with open('atm_software_db.txt', 'r') as read_data:
        data = read_data.read()
        new_line_data = data.split('\n')
        for datas in new_line_data:
            if datas:
                ac, name, email, mobile_number, password, balance = datas.split(',')
                if uid == ac and passw == password:
                    # print('Account is valid')
                    return True


def identity_confirmation(userid, password, default_life=3):
    identity_check = user_pass_check(userid, password)
    if identity_check:
        choice = input('Please enter your choice: \n'
                      '\t[1] Check balance\n'
                      '\t[2] Cash Out\n'
                      '\t[3] View all information\n'
                       '\t[4] Setting\n')
        if choice == '1':
            # flag = '1'
            all_information_check(userid, password, view_flag="1")
        elif choice == '2':
            current_balance = all_information_check(userid, password, view_flag='2')
            # cashout_amount = input('Enter amount to cash out: ')
            # update_balance = substraction(current_balance, cashout_amount)
            information_update(userid, password)
        elif choice == '3':
            # flag = '3'
            all_information_check(userid, password, view_flag="3")
        elif choice == "4":
            all_information_check(userid,password,view_flag="4")
    else:
        if default_life > 1:
            default_life -= 1
            print('\n'
                  '[✘] Account No or Password is incorrect.')
            print('You have {} chance left.'.format(default_life))
            identity_confirmation(userid, password, default_life)


def atm():
    account_confirmation = input('Do you have any account? (y/n): ').lower()
    userid = ''
    password = ''
    if account_confirmation == 'y':
        userid = input('Enter account number: ')
        password = input('Enter account password: ')
    while True:
        if account_confirmation == 'y':
            identity_confirmation(userid, password)
        else:
            account_creation_confirmation = input('You have no account associated with the account ID or Password.\n'
                                                  'Do you want to create one? (y/n): ').lower()
            if account_creation_confirmation == 'y':
                add_account()
            else:
                account_confirmation = input('Do you have any account? (y/n): ').lower()

        user_choice = input('Do you want to use it again? (y/n): ')
        if user_choice == 'n':
            print('Thanks for your visit.')
            break


if __name__ == '__main__':
    atm()
