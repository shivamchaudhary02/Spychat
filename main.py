from spy_details import spy
from datetime import datetime
f=datetime.now()
print f
from steganography.steganography import Steganography
print 'Hello'
print 'Let\'s get Started'

STATUS_MESSAGE =['Batman Superman Hanuman','Always B+','Never lose Hope']
friends=[{'name':'Shushant','age':22,'rating':3.2,'is_online':True},{'name':'Shivam','age':23,'rating':4.2,'is_online':True}]
def add_status(c_status):
    if c_status != None:
        print 'Your current status is ' + c_status
    else:
        print 'You dont have any status currently. '
    existing_status= raw_input('You want to select from old status? Y/N ')
    if existing_status.upper()=='N':
        new_status= raw_input('Enter your status: ')
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) +'. ' + old_status
            serial_no = serial_no + 1
        user_choice = input('Enter your choice:')
        new_status= STATUS_MESSAGE[user_choice - 1]
    updated_status = new_status
    return updated_status

def add_friend():
    frnd={
        'name':' ',
        'age':0,
        'rating':0.0,
        'is_online':True

         }
    frnd['name']= raw_input('What is your name? ')
    frnd['age']= input('what is your age? ')
    frnd['rating']= input('What is your rating? ')
    if len( frnd['name'])>2 and 12<frnd['age']<50 and frnd['rating']>spy['rating']:
        friends.append(frnd)

    else:
        print 'Friend cannt be added.'
    return len(friends)

def select_frnd():
    seriol_no = 1
    for frnd in friends:
        print str(seriol_no) +'. ' +frnd['name']
        seriol_no = seriol_no+1
    user_selected_frnd= input('Enter your choice. ')
    user_selected_frnd_index = user_selected_frnd - 1
    return user_selected_frnd_index


def send_message():
    selected_frnd = select_frnd()
    original_image = raw_input('what is the name of original image? ')
    secret_text = raw_input('what is your text? ')
    output_path= 'output.jpg'
    Steganography.encode(original_image,output_path,secret_text)
    print 'Messgae encoded'

def read_message():
    selected_frnd = select_frnd()
    output_path = raw_input('Which image you want to decode? ')
    secret_text = Steganography.decode(output_path)
    print 'secret text is: ' +secret_text

def start_chat(spy_name,spy_age,spy_rating):
    print 'Here are your options ' + spy_name
    current_status = None
    show_menu =True
    while show_menu:
        choice=input('what do you want to do? \n 1.Add a status \n 2. Add a spy friend \n 3. Send a message \n 4.Read a message \n 0.Exit')
        if choice==1:
            current_status = add_status(current_status)
            print 'Updated status is: ' + current_status
        elif choice==2:
            no_of_frnds = add_friend()
            print 'You have ' + str(no_of_frnds)+ ' friends'
        elif choice==3:
            send_message()
        elif choice == 4:
            read_message()
        elif choice == 0:
            show_menu = False
        else:
            print 'Invalid entry'




spy_exist = raw_input('Are you a new user? Y/N ')
if spy_exist.upper()=='N':
    print 'Welcome back %s age of %d having rating of %d. ' %(spy['name'],spy['age'],spy['rating'])
    start_chat(spy['name'],spy['age'],spy['rating'])
elif spy_exist.upper()=='Y':
    spy_name = raw_input('What is your Spy Name? ')
    if len(spy_name) > 0:
        print 'Welcome ' + spy_name+' Happy to see you again...'
        spy_salutation = raw_input('What should we call you Mr. or Ms.? ')
        if spy_salutation=='Mr.' or spy_salutation=='Ms.':
            spy_name = spy_salutation + ' ' + spy_name
            print 'Alright ' + spy_name + ' I\'d like to know a little bit more about...'
            spy_age = 0
            spy_rating = 0.0
            spy_is_online = True
            spy_age= input('What is your age? ')
            if 50>spy_age>20:
                print 'Your age is correct'
                spy_rating = input('What is your rating? ')
                if spy_rating>=5.0:
                    print 'Great Spy'
                elif 3.5<spy_rating<5.0:
                    print 'Average Spy '
                elif 2.5<spy_rating<=3.5:
                    print 'Bad Spy'
                else:
                    print 'Who hired you? '
                spy_is_online = True
                print "Authentication complete. \n Welcome %s age of %d and rating of %d Proud to have you onboard" %(spy_name,spy_age,spy_rating)
                start_chat(spy_name, spy_age, spy_rating)
            else:
                print 'Ypu are not eligible to be a Spy...'
        else:
            print'oopsss'
    else:
        print 'Oopssss Please provide a valid name.'
else:
    print 'Invalid Entry'