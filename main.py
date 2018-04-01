from spy_details import spy_name,spy_age,spy_rating

print 'Hello'
print 'Let\'s get Started'

def start_chat(spy_name,spy_age,spy_rating):
    print 'Here are your options ' + spy_name
    show_menu =True
    while show_menu:
        choice=input('what do you want to do? \n 1.Add a status \n 2. Add a spy friend \n 3. Send a message \n 4.Read a message \n 0.Exit')
        if choice==1:
            print 'Will add a status'
        elif choice==2:
            print 'will add a friend'
        elif choice==3:
            print 'will send a message'
        elif choice == 4:
            print 'write a message'
        elif choice == 0:
            show_menu = False
        else:
            print 'Invalid entry'




spy_exist = raw_input('Are you a new user? Y/N ')
if spy_exist.upper()=='N':
    print 'Welcome back %s age of %d having rating of %d. ' %(spy_name,spy_age,spy_rating)
    start_chat(spy_name,spy_age,spy_rating)
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