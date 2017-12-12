import os
import csv


def college():

    #College selections

    print('Welcome to the Minnestoa College Tuition Estimatior')
    print('Please select a college you plan on attending')
    print('0 - University of Minnesota Duluth')
    print('1 - University of Minnesota St. Cloud')
    print('2 - Univeristy of Minnesota Twin Cities')
    print('3 - Minnesota State University Mankato')
    print('4 - Minnesota State University Moorhead')
    print('5 - College of St. Scholastica')

    #Variables

    global tuition
    global n
    global k
    global r_b
    global a

    #add ValueError exception
    # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
    
    while True:
        try:
            k = int(input('Select a college: '))
        except (ValueError, NameError, TypeError):
            print("Enter a number 0 - 5")
            continue
        else:
            break

    #Data from www.collegedata.com

    if k == 0:
        n = ('University of Minnesota Duluth')
        tuition = (13344)
        r_b = (7608)
        a = (24424)
    elif k == 1:
        n = ('University of Minnesota St. Cloud')
        tuition = (8113)
        r_b = (8558)
        a = (20571)
    elif k == 2:
        n = ('Univeristy of Minnesota Twin Cities')
        tuition = (14417)
        r_b = (9852)
        a = (27469)
    elif k == 3:
        n = ('Minnesota State University Mankato')
        tuition = (8161)
        r_b = (8375)
        a = (18046)
    elif k == 4:
        n = ('Minnesota State University Moorhead')
        tuition = (8467)
        r_b = (8282)
        a = (20749)
    elif k == 5:
        n = ('College of St. Scholastica')
        tuition = (36212)
        r_b = (9522)
        a = (49104)

    #Tell them what college they selected and its cost of attendance
    print('You selected',n,'which cost $',tuition,'a year')
college()

#Choose a degree( Time variable )

def degree():

    global time
    global degree

    print('\nSelect your type of degree')
    print('0 - Bachelors degree(4 years)')
    print('1 - Masters degree(6 years)')
    print('2 - Doctorate degree(8 years)')
    w = input('Enter your selection: ')

    if w == '0':
        time = 4
        degree = ('Bachelors degree')
    if w == '1':
        time = 6
        degree = ('Masters degree')
    if w == '2':
        time = 8
        degree = ('Doctorate degree')
    print('You selected a',degree)
degree()

#Start of extra questions

def scholar():
    global scho
    while True:
        try:
            scho = int(input('\nEnter the amount you receive from Scholarsihps: '))
        except (ValueError, NameError, TypeError):
            print("Enter a number!")
            continue
        else:
            break
scholar()

def gaurd():
    
    global gt

    print('\nAre you in the national gaurd?')
    print('0 - yes')
    print('1 - no')

    k = input('Enter your selection: ')
    if k == '0':
        gt = 1
    elif k == '1':
        gt = tuition
gaurd()

def fas():
    
    global fasfa
    
    print('\nHow much do you recive for finacial student aid?')
    print('0 - $0')
    print('1 - less than $1,000')
    print('2 - 3,000+')
    print('3 - 5,000+')
    print('4 - 7,000+')
    print('5 - 10,000+')
    k = input('Enter your selection: ')

    if k == '0':
        fasfa = 0
    elif k == '1':
        fasfa = 1000
    elif k == '2':
        fasfa = 3000
    elif k =='3':
        fasfa = 5000
    elif k == '4':
        fasfa = 7000
    elif k =='5':
        fasfa = 10000    
fas()

def job():
    
    global per

    print('\nAre you going to have a job during college?')
    k = input('Enter yes or no: ')

    if k == 'yes':
        per = int(input('\nEnter amount(per month) towards college debt: '))
    elif k == 'no':
        per = 0
job()


def eq():
    
    global cost
    
    if tuition < 2:
        cost =  (r_b * time) - ((((per * (time*12)) + (fasfa * 4))) - scho)
    else:
        cost = ((gt + r_b)* time) - ((((per * (time*12)) + (fasfa * 4))) - scho)
eq()

print('\nThe total cost for a',degree,'at',n,'will cost: $',cost)

def csv():

    print('Would you like to import data into a spreadsheet?')
    print('Yes or no?')
    k = input()
    
    if k == 'yes' or 'Yes':
        import csv
        fname = 'TuitionCalculator.csv'
        f = open(fname,'w+')
        f.close()
        row1 = ['College name', n]
        row2 = ['Cost of attendance', a]
        row3 = ['Tuition', tuition]
        row4 = ['Room and Board', r_b]
        row5 = ['Degree', degree]
        row6 = ['Financial Aid', fasfa]
        row7 = ['Monthly job payments', per]
        row8 = ['Total cost', cost]
 

        with open('TuitionCalculator.csv', 'w+') as csvfile:
            w = csv.writer(csvfile)
            w.writerow(row1)
            w.writerow(row2)
            w.writerow(row3)
            w.writerow(row4)
            w.writerow(row5)
            w.writerow(row6)
            w.writerow(row7)
            w.writerow(row8)
        print('Thank you for using the Minnesota Tuition Claculator!')
            
    else:
        print('Thank you for using the Minnesota Tuition Claculator!')
        
csv()
#Add a pasue so it doesnt exit
os.system("pause")

