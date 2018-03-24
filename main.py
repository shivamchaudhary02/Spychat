print 'Hello'
print 'Let\'s get Started'
spy_name = raw_input('What is your Spy Name? ')
if len(spy_name) > 0:
    print 'Welcome ' + spy_name+' Happy to see you again...'
    spy_salutation = raw_input('What should we call you Mr. or Ms.? ')
    if spy_salutation=='Mr.' or spy_salutation=='Ms.':
        print spy_salutation
        spy_name = spy_salutation + ' ' + spy_name
        print spy_name
        print 'Alright ' + spy_name + ' I\'d like to know a little bit more about...'
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = True
        spy_age= input('What is your agre? ')
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
            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
        else:
            print 'Ypu are not eligible to be a Spy...'
    else:
        print'oopsss'
else:
    print 'Oopssss Please provide a valid name.'
