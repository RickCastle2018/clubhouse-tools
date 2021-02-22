from clubhouse.clubhouse import Clubhouse

if __name__ == "__main__":
    clubhouse = Clubhouse()

    #hello message
    print("clubhouse-tools / invite \n©2021 by Nikita Nikonov \n ")

    #user enters tel
    phone_number = input("Enter your phone number to login into Clubhouse: ")

    #send verification code
    clubhouse.start_phone_number_auth(phone_number)
    print("Verification code sent")

    #user enters sms verification code to login
    verification_code = input("Enter it: ")
    clubhouse.complete_phone_number_auth(phone_number, verification_code)

    #user enters phone number of user he wants to invite
    phone_number = input("Enter phone number of user you want to invite: ")
    name = input("Enter name of user you want to invite: ")
    clubhouse.invite_to_app(name, phone_number, message="Invited from clubhouse-invite")
