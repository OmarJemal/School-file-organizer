import os
import time
import shutil

#time.ctime(os.path.getmtime("Assign-5.pdf"))
#date = time.gmtime(os.path.getmtime("Assign-5.pdf"))

#print(date.tm_year)
#print(date.tm_mon)
#print(date.tm_mday)

def getDate():
    day = int(input('Please enter the day:'))
    month = int(input('Please enter the month:'))
    year = int(input('Please enter the year:'))

    return (day,month,year)

print(''' 
This program was designed to help organizing files for school. 
It takes an input of number of semesters and makes a folder for each semester.
The program asks about when each semester started and ended, and uses that information to sort the files.
''')

numberOfSemesters = input('How many new semesters did you want to sort?')
properNumber = int(numberOfSemesters)
folders = []

for i in range(0,properNumber):
    folders.append('Semester ' + str(i + 1))

#print(folders)
prevousEnd = (0,0,0)
startDate = (0,0,0)
EndDate = (0,0,0)


for i in range(0,properNumber):
    if( not (os.path.exists("./" + folders[i])  )  ):
        os.mkdir(folders[i])

    if(i != 0):
        choice = input('press y to use the end date of the prevous semester as the starting date for this one, and enter anything else to set a different start date')
        if(choice.upper() == 'Y'):
            EndDate = prevousEnd
        else:
            print('please enter the starting date')
            startDate = getDate()
    else:
        print('please enter the starting Date: \n')
        startDate = getDate()
        

    print('please enter the ending Date: \n')
    EndDate = getDate()
    prevousEnd = EndDate

    print(startDate)
    print(EndDate)
    input("paused")
    files = os.listdir()
    
    for j in range(0, len(files)):
        date = time.gmtime(os.path.getmtime(files[j]))

        

        if(date.tm_year >= startDate[2] and date.tm_year <= EndDate[2]):
           
            if(date.tm_mon >= startDate[1] and date.tm_mon <= EndDate[1]):
               # print('here')
                
                if(date.tm_mday >= startDate[0] and date.tm_mday <= EndDate[0]):
                    print('a file found!\n\n')
                    print(files[j])

                    scr = os.path.realpath(files[j])
                    head, tail = os.path.split(scr)
                    dst = head + '\\' + folders[i]
                    print('processing ' + tail + "...")
                    print('copying ' + tail + " to " + dst)
                    shutil.copy(scr, dst)
                    print('transferred ' + tail + ' to ' + dst + '\n')

"""  
date2 = time.gmtime(os.path.getmtime("Assign-5.pdf"))
print(date2.tm_year)
print(date2.tm_mon)
print(date2.tm_mday)
"""

"""
! - check mark
we need a part that makes the proper directory !
we need a part to look at all the relevent files !
we need a part to exclude certain files
we need a part to include certain files
we need a part that takes input from the user about the range of the dates the files should be in !
we need a part that moves the files to the right folder 
we need a part that makes the right amount of files move to the corresponding folder

eventually 
make a g.u.i. 
take user input to how many folders they want and what the names would be
what are some key words for the files that need to go to each folder
an option to add a key word for certain files each time it meets a certain critrea

mfdmf 
"""

